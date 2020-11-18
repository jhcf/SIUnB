
import urllib, json
from urllib.request import urlopen

def code_information_osm(overpass_id):
    url_open = f"https://api.openstreetmap.org/api/0.6/node/{overpass_id}.json"
    response_node = urlopen(url_open)
    data_node = json.loads(response_node.read())

    return data_node

def code_information_wiki(wikidata_code):
    url_wiki = f"https://www.wikidata.org/wiki/Special:EntityData/{wikidata_code}.json"
    response_wiki = urlopen(url_wiki)
    data_wiki = json.loads(response_wiki.read())
    return data_wiki

def main():
    print(code_information_osm(8127805812))
    print('\n')
    print(code_information_wiki('Q102037740'))

main()
