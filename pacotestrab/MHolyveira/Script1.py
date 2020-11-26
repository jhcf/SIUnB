import json
import sys
from fuzzywuzzy import fuzz
from SPARQLWrapper import SPARQLWrapper, JSON

#Retorna o Código que do item mais parecido com a consulta
def rank_names(name, dictItems):
    dictRank = {k:fuzz.ratio(name, v) for k,v in dictItems.items()}
    
    return  max(dictRank, key=dictRank.get)

#Faz o request SPARQL na API do Wikidata e retorna os valores em json
def request_wikidata(query):
    wikidata_url = "https://query.wikidata.org/sparql"
    user_agent = "WDQS-example Python/%s.%s" % (sys.version_info[0], sys.version_info[1])
    sparql = SPARQLWrapper(wikidata_url, agent=user_agent)
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)

    return sparql.query().convert()

#Retorna todos os eventos dada uma location em formato: 'Q102104636'
def get_events( location):
    query = f'''
    SELECT ?evento ?eventoLabel 
    WHERE {{
      ?evento wdt:P276 wd:{location}.
      SERVICE wikibase:label {{ bd:serviceParam wikibase:language "pt-br" }}.
    }}
    '''
    return request_wikidata(query)

#Retorna a localização data uma string de consulta ex: "Teatro de arena da UnB" retorna "Q101526639"
def get_location(search):
    search = search.lower()
    query = f'''
    SELECT ?item ?itemLabel
        WHERE {{ 
        ?item wdt:P31 wd:Q41176.
        ?item rdfs:label ?itemLabel. 
        FILTER(CONTAINS(LCASE(?itemLabel), '{search}')). 
        }} limit 100'''
    json = request_wikidata(query)
    dictItems = {}
    for item in json["results"]["bindings"]:
        cod = item["item"]["value"][31:]# código Q6150120
        label = item["itemLabel"]["value"].lower()# nome do edifício
        dictItems[cod] = label

    location = rank_names(search, dictItems)
    
    return location
   
search = "teatro de arena"

location = get_location(search) #Teatro de arena da UnB
events = get_events(location)

print(events)