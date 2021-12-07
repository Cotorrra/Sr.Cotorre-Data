import json

from flask import (
    Flask,
    request,
    Response
)
from waitress import serve


app = Flask(__name__)


@app.route('/', methods=['GET'])
def tarot():
    try:
        language = request.args.get("language")
        call_type = request.args.get("type")
    except:
        return "Bad Request", 400

    file_src = f'data/{language}/{call_type}.json'
    with open(file_src, "r", encoding='utf-8') as pack:
        response = json.load(pack)

    response = json.dumps(response)

    return Response(response, mimetype='application/json')


serve(app, host="0.0.0.0", port=8080)