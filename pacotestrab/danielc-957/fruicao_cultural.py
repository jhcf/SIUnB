from SPARQLWrapper import SPARQLWrapper, JSON
import json
import sys
from urllib.request import urlopen
import requests
import datetime


WIKIDATA_URL = "https://www.wikidata.org"

def code_information_wiki(wikidata_code):
    url_open = f'{WIKIDATA_URL}/wiki/Special:EntityData/{wikidata_code}.json'
    response_node = urlopen(url_open)
    data_wiki = json.loads(response_node.read())
    return data_wiki

def code_information():
    sparql = SPARQLWrapper("https://query.wikidata.org/sparql")
    receive_name = sys.argv[1]

    key_search = '\"' + receive_name + '\"'

    query = """
    SELECT ?item ?itemLabel WHERE {
    SERVICE wikibase:mwapi {
        bd:serviceParam wikibase:endpoint "www.wikidata.org";
            wikibase:api "EntitySearch";
            mwapi:search """ + key_search + """; # Search for things named "soriano"
            mwapi:language "en".
        ?item wikibase:apiOutputItem mwapi:item.
    }
    MINUS {
        ?item wdt:P31 wd:Q5 . # but MINUS or negate any of those things that are instances of human
    }
    SERVICE wikibase:label {bd:serviceParam wikibase:language "pt-br".}
    }
    LIMIT 100
    """

    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    return results

def write_json(file):
    with open('info.json', 'w', encoding='utf-8') as f:
        json.dump(file, f, ensure_ascii=False, indent=4)

def write_txt(file):
  with open('info.txt', 'w') as filehandle:
    for listitem in file:
        filehandle.write('%s\n' % listitem)


def format_date(date):
    new_date =  date[9:-10] +  "-" + date[6:-13] + "-" + date[1:-16]
    return new_date

def get_event_reference(place,wiki_data,ref_receive_number):
    try:
        get_lenght_events = len(wiki_data ["entities"] [place] ["claims"] ["P793"])
        get_event_code = wiki_data ["entities"] [place] ["claims"] ["P793"] [ref_receive_number] ["mainsnak"] ["datavalue"] ["value"] ["id"]
        return get_event_code
    except :
        print("Evento Buscado nao foi encontrado!")
        print("\n")
        sys.exit(0)
    # print(get_event_code)

#Pega os codigos wiki da api
def search_hour(event_detais,get_event_code):
    try: 
        hour_init = event_detais ["entities"] [get_event_code] ["claims"] ["P585"] [0] ["references"] [0] ["snaks"] ["P4241"] [0] ["datavalue"] ["value"] ["id"]  
        final_hour = event_detais ["entities"] [get_event_code] ["claims"] ["P585"] [0] ["references"] [0] ["snaks"] ["P4241"] [1] ["datavalue"] ["value"] ["id"]
        return hour_init,final_hour
    except: 
        print("-Nao possui horarios cadastrados")
        error_hour_init = 0
        error_final_hour = 0
        return error_hour_init,error_final_hour
        

def return_hour(hour_init,final_hour):
    data_hour_init = code_information_wiki(hour_init)
    data_hour_final = code_information_wiki(final_hour)
    return_hour_init = data_hour_init ["entities"] [hour_init] ["labels"] ["en"] ["value"]
    return_hour_final = data_hour_final ["entities"] [final_hour] ["labels"] ["en"] ["value"]
    if (return_hour_init == "9 AM"):
        return_hour_init = "09:00"
    return return_hour_init,return_hour_final
    
def search_promoter(event_details,get_event_code):
    promoter_place = event_details ["entities"] [get_event_code] ["claims"] ["P131"] [0] ["mainsnak"] ["datavalue"] ["value"] ["id"]
    return promoter_place 

def return_promoter_place(code_wiki_promoter):
    try: 
        promoter = code_information_wiki(code_wiki_promoter)
        return_final_promoter = promoter ["entities"] [code_wiki_promoter] ["labels"] ["pt-br"] ["value"]

    except:
        print("promoter entrou aqui")
        return_final_promoter = "Nao informado"
    #print(return_final_promoter)

    return return_final_promoter

def find_social_links(event_details,get_event_code):
    try: 
        lenght_media = len(event_details ["entities"] [get_event_code] ["claims"] ["P31"] [0] ["references"])
        count = 0
        links = []
        while (count < lenght_media):
            add_list = event_details ["entities"] [get_event_code] ["claims"] ["P31"] [0] ["references"] [count] ["snaks"] ["P854"] [0] ["datavalue"] ["value"]
            links.append(add_list)
            count = count + 1
        return links
    except: 
        links = []
        links.append("Links nao informados")


def get_event_details(place,wiki_data,ref_receive_number):
    get_event_code = get_event_reference(place,wiki_data,ref_receive_number)
    event_detais = code_information_wiki(get_event_code)
    event_name = event_detais ["entities"] [get_event_code] ["labels"] ["pt-br"] ["value"]  
    try: 
        event_daytime = event_detais ["entities"] [get_event_code] ["claims"] ["P585"] [0] ["mainsnak"] ["datavalue"] ["value"] ["time"]
        # print('\n') 
        date_event = format_date(event_daytime)
    except: 
        print("O evento nao possui hora definida")
        date_event = "Nao informado"
    
    final_hours =  search_hour(event_detais,get_event_code)
    if (final_hours[0] == 0  and final_hours[1] == 0 ):
        final_info_hours = "Nao informado"
    else:    
        new_return_hours = return_hour (final_hours[0],final_hours[1])
        final_info_hours = new_return_hours[0] + " horas - " + new_return_hours[1] + " horas"
        find_promoter = search_promoter(event_detais,get_event_code)
        promoter_final = return_promoter_place(find_promoter)
        links = find_social_links(event_detais,get_event_code)
        #print(event_detais)
    return event_name,date_event,final_info_hours,promoter_final,links

def main(): 
    receive_number = sys.argv[2]
    ref_receive_number = 0
    if (receive_number == 0):
        ref_receive_number = 1
    else:
        ref_receive_number =  int(receive_number) - 1  
    #print(ref_receive_number)
    get_code_information = code_information()
    #print(get_code_information)
    #print('\n')
    local_event = get_code_information ["results"] ["bindings"] [0] ["itemLabel"] ["value"] 
    base_wiki_code = get_code_information ["results"] ["bindings"] [0] ["item"] ["value"]
    wiki_code = base_wiki_code[31:]
    #print(wiki_code)
    #print('\n')
    wiki_data = code_information_wiki(wiki_code)
    #print(wiki_data)
    info_list = get_event_details(wiki_code,wiki_data,ref_receive_number)
    try:
        event = info_list[0]
        date = info_list[1]
        hour = info_list[2]
        promoter = info_list[3]
        links = info_list [4]
        #print(info_list)
        print("Local: "  + local_event)
        print("Evento: " + event)
        print("Data: " + date)
        print("Hora: " + hour)
        print("Promotor: " + promoter)
        print("Comentarios obtidos nas midias sociais: ")
        for index in range(len(links)):
            print(links[index])

    except:
        print("Local: "  + local_event)
        print("Evento: " + event)
        print("Data: " + date)
        print("Hora: " + hour)
        print("Promotor: " + promoter)
        print("Comentarios obtidos nas midias sociais: ") 
        for index in range(len(links)):
            print(links[index])

    final_information_list = []
    information_dict = {
        "local_event": local_event,
        "event": event,
        "date": date,
        "hour": hour,
        "promoter": promoter,
        "links:": links
    }

    final_information_list.append(information_dict)
    write_json(final_information_list[0])
    write_txt(final_information_list)

main()
