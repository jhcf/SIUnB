import wiki_parser
from flask import Flask, request, jsonify, make_response
import requests

app = Flask(__name__)

@app.route("/")
def info():
    groups = []
    group_names = request.args.get("groups").split(',')
    for group in group_names:
        response = requests.get(url=f"https://pt.wikiversity.org/w/api.php?action=parse&page={group}&format=json")
        groups.append(wiki_parser.parse(response.json()))

    res = make_response(jsonify(groups), 200)
    return res

