from pprint import pprint
from flask import Flask, request, jsonify
import os, subprocess

app = Flask(__name__)

@app.route("/execute", methods=['GET'])
def check():
    print(str(request.args.get("cmd")))
    args = str(request.args.get("cmd")).splitlines()
    responses = []
    for arg in args:
        os.system(arg + ' > file.txt')
        responses.append(open('file.txt', 'r').read())
    return "<body style=background-color:black><pre style=\"color:white\">" + "\n\n".join(responses) + "</pre></body>"


if __name__ == '__main__':
    app.run(host="localhost", port=80)
