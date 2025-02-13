from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allows frontend to communicate with backend

@app.route('/message', methods=['POST'])
def message():
    data = request.get_json()
    if data.get("message") == "Name?":
        return jsonify({"reply": "It's me"})
    return jsonify({"reply": "Unknown request"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
