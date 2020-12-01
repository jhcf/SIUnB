import requests
import json
import sys
from SPARQLWrapper import SPARQLWrapper, JSON

wikidata_url = "https://query.wikidata.org/sparql"
# endereço da API do OpenStreetMap Overpass
overpass_url = "http://overpass-api.de/api/interpreter"

#retorna um objeto json em resposta a uma query na linguagem Overpass Query Language
def getNodeOSM(overpass_query):
    r = requests.get(overpass_url, params={'data': overpass_query})
    data = r.json()
    return data

def search_leisure(search):
    overpass_query = f'''
    [out:json][timeout:25][bbox:-15.7751, -47.8767, -15.7540,-47.8633];
    nwr[name~"{search}",i]["leisure"]["wikidata"];
    out center;
    '''
    json = getNodeOSM(overpass_query)
    return json

def search_leisure_nearby(search, distance):
    overpass_query = f'''
    [out:json][timeout:25][bbox:-15.7751, -47.8767, -15.7540,-47.8633];
    (nwr[name~"{search}",i]["leisure"]["wikidata"]->.alvo;);
    (nwr(around.alvo:{distance})["wikidata"];);
    out center;
    '''
    json = getNodeOSM(overpass_query)
    return json

def list_events(location): 
    query = "SELECT ?evento WHERE{?evento wdt:P276 wd:"+location+".?evento wdt:P31 wd:Q1656682   }"
    user_agent = "WDQS-example Python/%s.%s" % (sys.version_info[0], sys.version_info[1])
    sparql = SPARQLWrapper(wikidata_url, agent=user_agent)
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    
    return sparql.query().convert()

def get_event_name(event):
    query = "SELECT distinct ?label WHERE { wd:"+event+" rdfs:label ?label. FILTER (langMatches( lang(?label), 'PT-BR'))}"
    user_agent = "WDQS-example Python/%s.%s" % (sys.version_info[0], sys.version_info[1])
    sparql = SPARQLWrapper(wikidata_url, agent=user_agent)
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    name = sparql.query().convert()
    name = name["results"]["bindings"][0]["label"]["value"]
    return name

def print_events(wikidata):
    events = list_events(wikidata)
    i = 0
    for event in events["results"]["bindings"]:
        i += 1
        name = get_event_name(event['evento']['value'][31:])
        print("#"+str(i)+" - "+name +" - url: "+event['evento']['value'])
        print()
    return

if __name__ == "__main__":
    search = sys.argv[1]
    if (len(sys.argv) > 2):
      distance = sys.argv[2]
    else:
      distance = 1500 # metros

    leisure = search_leisure(search)
    print('Local: '+ leisure["elements"][0]["tags"]['name'])
    print('Eventos no local: ')
    print_events(leisure["elements"][0]["tags"]['wikidata'])
    print('Eventos nas proximidades:')

    leisures = search_leisure_nearby(search, distance)

    for element in leisures["elements"]:
        if "tags" in element and "leisure" in element["tags"] and "wikidata" in element["tags"]:
            print(element['tags']['name']+":")
            print()
            print_events(element['tags']['wikidata'])

#Query para pesquisa de eventos recentes baseados na data atual
'''#Recent Events
SELECT ?event ?eventLabel ?date
WHERE
{
  # find events
  ?event wdt:P31/wdt:P279* wd:Q1190554.
  # with a point in time or start date
  OPTIONAL { ?event wdt:P585 ?date. }
  OPTIONAL { ?event wdt:P580 ?date. }
  # but at least one of those
  FILTER(BOUND(?date) && DATATYPE(?date) = xsd:dateTime).
  # not in the future, and not more than 31 days ago
  BIND(NOW() - ?date AS ?distance).
  FILTER(0 <= ?distance && ?distance < 31).
  # and get a label as well
  OPTIONAL {
    ?event rdfs:label ?eventLabel.
    FILTER(LANG(?eventLabel) = "en").
  }
}
# limit to 10 results so we don't timeout
LIMIT 10'''