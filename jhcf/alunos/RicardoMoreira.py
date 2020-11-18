import requests
OPENSTREEMAP_URL = "https://api.openstreetmap.org/api/0.6"
WIKIDATA_URL = "https://www.wikidata.org"

def getNode(id: int):
  url = f'{OPENSTREEMAP_URL}/node/{id}.json'
  r = requests.get(url=url)
  data = r.json()
  return data

def getEntity(id: str):
  url = f'{WIKIDATA_URL}/wiki/Special:EntityData/{id}.json'
  r = requests.get(url=url)
  data = r.json()
  return data

print(getNode(8115231044))
print(getEntity('Q101555073'))
