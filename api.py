from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

# Enable CORS with more explicit configuration
CORS(app, resources={
    r"/*": {
        "origins": "*",  # In production, replace with your GitHub Pages domain
        "methods": ["POST", "OPTIONS"],
        "allow_headers": ["Content-Type"]
    }
})

@app.route('/ask-name', methods=['POST', 'OPTIONS'])
def ask_name():
    # Handle preflight OPTIONS request
    if request.method == 'OPTIONS':
        response = app.make_default_options_response()
        response.headers.add('Access-Control-Allow-Origin', '*')  # For development
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        response.headers.add('Access-Control-Allow-Methods', 'POST')
        return response

    try:
        data = request.get_json()
        
        if data and data.get('message') == "Name?":
            response = jsonify({'response': "It's me"})
        else:
            response = jsonify({'response': "Invalid request"}), 400
            
        # Explicitly add CORS headers to the response
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
        
    except Exception as e:
        app.logger.error(f"Error processing request: {str(e)}")
        return jsonify({'error': 'Internal server error'}), 500

@app.after_request
def after_request(response):
    # Ensure CORS headers are added to all responses
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    response.headers.add('Access-Control-Allow-Methods', 'POST')
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
