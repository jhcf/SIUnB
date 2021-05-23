import json
import sys

def getQCodes(data):
    manifestCulturais = data['groups'][1:]

    events = []

    for manifCultural in manifestCulturais:

        events = events + [manifCultural['events']]

    wikidataEntries = []

    for event in events:

        wikidataEntries = wikidataEntries + event[0]['wikidata']

    qCodes = []
    for entry in wikidataEntries:
        dataPointIndex = entry.index("Q")
        
        qCodes = qCodes + [entry[dataPointIndex: ]]

    return qCodes

def renderIFrame(qCodes):
    htmlHead = """<iframe style="width: 100vw; height: 100vh; border: none;" src="https://query.wikidata.org/embed.html#%23defaultView%3AGraph%0ASELECT%20%3Fevent%20%3FeventLabel%20WHERE%20%7B%0A%20%20SERVICE%20wikibase%3Alabel%20%7B%20bd%3AserviceParam%20wikibase%3Alanguage%20%22%5BAUTO_LANGUAGE%5D%2Cen%22.%20%7D"""

    qCodePreamble = "%0A%20%20%7B%20%3Fevent%20wdt%3A*%20wd%3A"
    
    unionCode = "%20%7D%0A%20%20UNION"

    htmlTail = '%20%7D%0A%7D%0ALIMIT%20100" referrerpolicy="origin" sandbox="allow-scripts allow-same-origin allow-popups"></iframe>'

    for qCode in qCodes[:-1]:
        
            htmlHead = htmlHead + qCodePreamble + qCode + '.'
            htmlHead = htmlHead + unionCode

    htmlHead = htmlHead + qCodePreamble + qCodes[-1] + '.' + htmlTail

    return htmlHead

def renderHtml(iframe):
    htmlFile ="""<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
  </head>
  <body>
    """

    htmlTail = """
  </body>
</html>"""

    htmlFile = htmlFile + semanticsFrame

    htmlFile = htmlFile + htmlTail

    return htmlFile

if (len(sys.argv) == 1): #Mostra o uso correto do script no terminal
    print("\nUso: $ python3 getSemantics.py source.json \n")
else:

    inputJson = sys.argv[1]

    with open(inputJson) as f:
        data = json.load(f)
    f.close()
    
    qCodes = getQCodes(data)
    
    semanticsFrame = renderIFrame(qCodes)

    htmlFile = renderHtml(semanticsFrame)

    f = open("semanticsView.html", "w")
    f.write(htmlFile)
    f.close()



