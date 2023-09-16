# app.py
from flask import *
import sys
from generate_response import generate_response, txtToString

app = Flask(__name__)


@app.route("/")
def home():
    resp = Response(response=json.dumps({"text": "home1"}))
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


@app.route('/post', methods=['POST'])
def handle_request():
    content = request.data.decode('utf-8')

    results = generate_response(content, 'medication-reader-openai/text_files/examples.txt', 
                                'medication-reader-openai/text_files/text_guidelines.txt')
    resp = Response(response=json.dumps({"content": results}))
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


if __name__ == "__main__":
    app.run(debug=True)
