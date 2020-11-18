import requests

OSM_URL = "https://api.openstreetmap.org/api/0.6"
WD_URL = "https://www.wikidata.org"


def getNode(id: int):
 url = f"{OSM_URL}/node/{id}.json"
 r = requests.get(url=url)
 data = r.json()
 return data

def getEntity(id: str):
  url = f"{WD_URL}/wiki/Special:EntityData/{id}.json"
  r = requests.get(url=url)
  data = r.json()
  return data

print(getNode(8121922843))
print(getEntity("Q101864759"))
