from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/ask-name', methods=['POST'])
def ask_name():
    data = request.get_json()
    
    if data and data.get('message') == "Name?":
         response = flask.jsonify({'response': "It's me"})
         response.headers.add('Access-Control-Allow-Origin', '*')
         return response
    
    return jsonify({'response': "Invalid request"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
