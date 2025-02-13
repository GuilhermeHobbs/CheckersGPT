from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enables CORS so GitHub Pages can access this API

@app.route('/ask', methods=['GET'])
def ask():
    return jsonify({"answer": "It's me"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
