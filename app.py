from flask import Flask, request, jsonify, make_response
from flask_cors import CORS

app = Flask(__name__)

# List of allowed origins
ALLOWED_ORIGINS = [
    'https://guilhermehobbs.github.io/',  # Replace with your GitHub Pages domain
    'http://localhost:5000',  # For local testing
    'http://127.0.0.1:5000'   # For local testing
]

# Configure CORS with specific origins
CORS(app, resources={
    r"/ask-name": {
        "origins": ALLOWED_ORIGINS,
        "methods": ["POST", "OPTIONS"],
        "allow_headers": ["Content-Type"]
    }
})

@app.route('/ask-name', methods=['POST', 'OPTIONS'])
def ask_name():
    origin = request.headers.get('Origin')
    
    # Handle preflight OPTIONS request
    if request.method == 'OPTIONS':
        response = make_response()
        if origin in ALLOWED_ORIGINS:
            response.headers.add('Access-Control-Allow-Origin', origin)
            response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
            response.headers.add('Access-Control-Allow-Methods', 'POST')
        return response

    data = request.get_json()
    
    if data and data.get('message') == "Name?":
        response = make_response(jsonify({'response': "It's me"}))
    else:
        response = make_response(jsonify({'response': "Invalid request"}), 400)
    
    # Add CORS headers to the actual response
    if origin in ALLOWED_ORIGINS:
        response.headers.add('Access-Control-Allow-Origin', origin)
    
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
