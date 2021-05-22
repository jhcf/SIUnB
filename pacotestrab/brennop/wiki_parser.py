import xml.etree.ElementTree as ET
import datetime

key_dict = {
    'OSM': 'osm',
    'Wikidata': 'wikidata',
    'Wikipedia': 'wikipedia',
    'Facebook': 'facebook',
    'Instagram': 'instagram',
    'Twitter': 'twitter',
    'Youtube': 'youtube',
    'Teams': 'teams',
    'Stream': 'stream',
}

def parse(data):
    result = {}

    # se não há parse, é provalmente um erro, retorna o erro
    if "parse" not in data:
        return data

    html = data["parse"]["text"]["*"]
    document_tree = ET.fromstring(html)

    result["name"] = data["parse"]["title"]

    description = getSection(document_tree, "Descrição")
    # pode ser interessante buscar o html inteiro dessa seção para manter a marcação
    # nesse caso devemos serializar de volta a html ao invés de pegar o inner text
    result["description"] = "".join(description.itertext())

    members = getSection(document_tree, "Membros")
    result["members"] = list(extractLinks(members))

    api = getSection(document_tree, "API")
    result["api"] = next(extractLinks(api), None)

    # procura por captions
    # se as captions estiverem incorretas, podemos buscar pelas seções, mas não foi implementado
    for table in document_tree.findall('table'):
        if table[0].text.strip() == "Eventos":
            result["events"] = formatTable(table[1])
        elif table[0].text.strip() == "Acervo":
            result["assets"] = formatTable(table[1])
        elif table[0].text.strip() == "Serviços":
            result["services"] = formatTable(table[1])
    
    return result

def formatTable(data: ET.Element) -> list:
    result = []

    table_header = list(data[0])

    for row in data[1:]:
        table_elements = zip(table_header, row)
        entry = {}
        for head, value in table_elements:
            title = head.text.strip() 
            if title == "Nome":
                entry["name"] = value.text
            elif title == "Descrição":
                entry["description"] = value.text
            elif title == "Categorias":
                entry["categories"] = value.text.split(',') if value.text else []
            elif title == "Condições de Uso":
                entry["usage"] = value.text
            elif title == "Data":
                for date in value.text.split(','):
                    entry["days"] = datetime.datetime.strptime(date, "%Y-%m-%d").isoformat()
            elif title == "Dias de Oferta":
                entry["days"] = value.text.split(',') if value.text else []
            elif title == "Horários":
                entry["timeinterval"] = value.text
            else:
                if title:
                    entry[key_dict[title]] = list(extractLinks(value))
        result.append(entry)

    return result
             

def extractLinks(element: ET.Element):
    return map(lambda e: e.attrib["href"], element.findall('.//a'))

def getSection(root: ET.Element, name: str) -> ET.Element:
    content = ET.Element('')
    state = 'searching' # ou é searching ou é filling
    for el in root:
        # h2 separam as seções, ou vai parar ou vai iniciar
        if el.tag == "h2": 
            # se estiver procurando e achou um span com name começa a preencher
            if state == 'searching' and el.find(f"./[span='{name}']"):
                state = 'filling'
            # se estivesse preenchendo, chegamos ao fim da seção
            elif state == 'filling':
                break
        elif state == 'filling':
            content.append(el)

    return content
