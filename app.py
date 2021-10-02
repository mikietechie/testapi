from flask import Flask, jsonify, request
from flask_cors import CORS
import json


app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route("/api/ping", methods=['GET', 'POST'])
def ping():
    data = json.loads(request.get_json())
    print(data)
    return jsonify({"pong": data})

if __name__ == '__main__':
    app.run()
    