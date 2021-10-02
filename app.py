'''
By Mike Zinyoni
https://github.com/mikietechie
'''
from flask import Flask, jsonify, request
from flask_cors import CORS
import json, sys


app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route("/api/ping", methods=['GET', 'POST'])
def ping():
    try:
        data = json.loads(request.get_json())
    except:
        data = "No data!"
    print(data)
    return jsonify({"pong": data})

if __name__ == '__main__':
    try:
        port = int(sys.argv[1])
    except: # value error or index error
        port = 8000
    app.run(port=port)
    