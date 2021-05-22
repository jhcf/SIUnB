import json
import wiki_parser

with open('example2.json', 'r', encoding ='utf8') as json_file:
    result = wiki_parser.parse(json.loads(json_file.read()))


print(json.dumps(result))

