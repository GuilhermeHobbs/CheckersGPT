from flask import Flask, request, jsonify, make_response
from flask_cors import CORS

app = Flask(__name__)

# Basic CORS setup
CORS(app)

@app.route('/ask-name', methods=['POST', 'OPTIONS'])
def ask_name():
    # Handle preflight OPTIONS request
    if request.method == 'OPTIONS':
        response = make_response()
        response.headers.add("Access-Control-Allow-Origin", "https://railway.app")
        response.headers.add("Access-Control-Allow-Headers", "Content-Type")
        response.headers.add("Access-Control-Allow-Methods", "POST")
        return response

    data = request.get_json()
    
    if data and data.get('message') == "Name?":
        response = make_response(jsonify({'response': "It's me"}))
    else:
        response = make_response(jsonify({'response': "Invalid request"}), 400)
        
    # Add CORS headers to the actual response
    response.headers.add("Access-Control-Allow-Origin", "https://railway.app")
    return response

# Global after_request handler
@app.after_request
def add_cors_headers(response):
    response.headers.add("Access-Control-Allow-Origin", "https://railway.app")
    response.headers.add("Access-Control-Allow-Headers", "Content-Type")
    response.headers.add("Access-Control-Allow-Methods", "POST")
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
