from flask import Flask, request, jsonify, make_response
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/message', methods=['POST'])
def message():
    data = request.get_json()
    response = jsonify({"reply": "It's me" if data.get("message") == "Name?" else "Unknown request"})
    response.headers.add("Access-Control-Allow-Origin", "*")  # Allow CORS for all
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
