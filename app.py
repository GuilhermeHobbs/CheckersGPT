from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow all domains

@app.route('/message', methods=['POST'])
def message():
    data = request.get_json()
    response = jsonify({"reply": "It's me" if data.get("message") == "Name?" else "Unknown request"})
    
    # Explicitly set CORS headers
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Headers", "Content-Type,Authorization")
    response.headers.add("Access-Control-Allow-Methods", "POST,OPTIONS")

    return response

@app.route('/', methods=['GET'])
def home():
    return "Flask API is running!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
