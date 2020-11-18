import requests
import json
import sys
# endereço da API do OpenStreetMap Overpass
overpass_url = "http://overpass-api.de/api/interpreter"

#retorna um objeto json em resposta a uma query na linguagem Overpass Query Language
def getNodeOSM(overpass_query):
    r = requests.get(overpass_url, params={'data': overpass_query})
    data = r.json()
    return data

# recebe uma string com um fragmento do nome de um objeto OSM localizado no bouding box da UnB
# retorna o json dos objetos de interesse cultural localizados nas proximidades
def busca_equipamentos_culturais(location_name, distancia_metros):
    overpass_query = f'''
     [out:json][timeout:25];
     (
        way(-15.7751, -47.8767, -15.7540,-47.8633 )["leisure"]["wikidata"]["name"~"{location_name}",i];
        node(-15.7751, -47.8767, -15.7540,-47.8633 )["leisure"]["wikidata"]["name"~"{location_name}",i];
        rel(-15.7751, -47.8767, -15.7540,-47.8633 )["leisure"]["wikidata"]["name"~"{location_name}",i];
        )->.alvo;
      (
        way(around.alvo:{distancia_metros})["leisure"]["wikidata"];
        node(around.alvo:{distancia_metros})["leisure"]["wikidata"];
        rel(around.alvo:{distancia_metros})["leisure"]["wikidata"];
      );
      out body;
      >;
      out skel qt;
    '''
    print(overpass_query)
    print()
    json = getNodeOSM(overpass_query)
    return json

if __name__ == "__main__":
    # recebe como argumentos o nome aproximado do alvo e a distância em metros para busca
    # por equipamentos culturais próximos
    nome_alvo_inicial = sys.argv[1]
    if (len(sys.argv) > 2):
      distancia = sys.argv[2]
    else:
      distancia = 1500 # metros
    json = busca_equipamentos_culturais(nome_alvo_inicial, distancia)  
    for element in json["elements"]:
      if "tags" in element:
        if "leisure" in element["tags"]:
          if "wikidata" in element["tags"]:
            print(element['tags']['name'],' ',element['tags']['wikidata'])
 
