import requests
import json
import sys
overpass_url = "http://overpass-api.de/api/interpreter"

def getNodeOSM(overpass_query):
    r = requests.get(overpass_url, params={'data': overpass_query})
    data = r.json()
    return data

def main(location_name):
    overpass_query = f""" [out:json][timeout:25]; ( way(-15.7751, -47.8767, -15.7540,-47.8633 )["leisure"]["wikidata"]["name"~"{location_name}",i]; node(-15.7751, -47.8767, -15.7540,-47.8633 )["leisure"]["wikidata"]["name"~"{location_name}",i]; rel(-15.7751, -47.8767, -15.7540,-47.8633 )["leisure"]["wikidata"]["name"~"{location_name}",i];)->.alvo; ( way(around.alvo:1500)["leisure"]["wikidata"]; node(around.alvo:1500)["leisure"]["wikidata"]; rel(around.alvo:1500)["leisure"]["wikidata"];); out body; >; out skel qt; """ 
    overpass_query = f"""
[out:json][timeout:25];
(
  way(-15.7751, -47.8767, -15.7540,-47.8633 )["leisure"]["wikidata"]["name"~"{location_name}",i];
  node(-15.7751, -47.8767, -15.7540,-47.8633 )["leisure"]["wikidata"]["name"~"{location_name}",i];
  rel(-15.7751, -47.8767, -15.7540,-47.8633 )["leisure"]["wikidata"]["name"~"{location_name}",i];
  )->.alvo;
(
  way(around.alvo:1500)["leisure"]["wikidata"];
  node(around.alvo:1500)["leisure"]["wikidata"];
  rel(around.alvo:1500)["leisure"]["wikidata"];
);
out body;
>;
out skel qt;
    """ 
    print(overpass_query)
    print()
    json = getNodeOSM(overpass_query)
    for element in json["elements"]:
      if "tags" in element:
        if "leisure" in element["tags"]:
          if "wikidata" in element["tags"]:
            print(element['tags']['name'],' ',element['tags']['wikidata'])

    
if __name__ == "__main__":
    main(sys.argv[1])  
 
