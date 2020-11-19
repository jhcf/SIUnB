import requests
import json
import sys
from SPARQLWrapper import SPARQLWrapper, JSON

overpass_url = "http://overpass-api.de/api/interpreter"
wikidata_url = "https://query.wikidata.org/sparql"

def getNode(x,y):
    query = f"""
    [out:json];
    (
    node({x}, {y},{x}, {y});
    <;
    );
    out meta;"""

    r = requests.get(overpass_url,params={'data': query})
    data = r.json()
    return data

def getEvents(wikidata_url, location):

    query = f'''
    SELECT ?evento ?eventoLabel 
    WHERE {{
      ?evento wdt:P276 wd:{location}.
      SERVICE wikibase:label {{ bd:serviceParam wikibase:language "pt-br" }}.
    }}
    '''
    print(query)
    user_agent = "WDQS-example Python/%s.%s" % (sys.version_info[0], sys.version_info[1])
    sparql = SPARQLWrapper(wikidata_url, agent=user_agent)
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    return sparql.query().convert()

location = "Q102104636" #Auditório de Música da UnB

results = getEvents(wikidata_url, location)
data_json = getNode(-15.7644830, -47.8718000)

#print(json.dumps( data_json,indent=4))
print(data_json['elements'][0]['tags']['name']) #Recuperando o nome do JSON

for result in results["results"]["bindings"]:
    print(result)
