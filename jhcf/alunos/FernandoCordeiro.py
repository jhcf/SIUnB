
import requests
import json

overpass_url = "http://overpass-api.de/api/interpreter"
wikidata_url = "https://www.wikidata.org"

def getNodeOSM():                                                       # Retorna um arquivo .json
    overpass_query = """
    [out:json];
    (
    node(-15.76424,-47.86865,-15.76414,-47.86853);      
    <;
    );
    out meta;
    """                                                                 # Coordenadas (Sul,Oest,Norte,Leste) do CaAgro
    r = requests.get(overpass_url,                                      # Acesso aos dados dentro do Open Street Map
                            params={'data': overpass_query})
    data = r.json()

    return data

def getDataWK(id: str):                                                  # Retorna um arquivo .json
    json_url = f"{wikidata_url}/wiki/Special:EntityData/{id}.json"

    r = requests.get(url=json_url)
    data = r.json()

    return data

def main():
    print(getNodeOSM(),'\n')                                             # OpenStreetMap CaAgroUnB
    print(getDataWK("Q102043581"))                                       # Wikidata CaAgroUnB

if __name__ == "__main__":
    main()  
 