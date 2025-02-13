from flask import Flask, request, jsonify, make_response
from functools import wraps

app = Flask(__name__)

def cors_middleware(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        response = make_response(f(*args, **kwargs))
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Methods'] = 'POST'
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
        return response
    return decorated_function

@app.route('/ask-name', methods=['POST'])
@cors_middleware
def ask_name():
    try:
        data = request.get_json()
        if data and data.get('message') == "Name?":
            return jsonify({'response': "It's me"})
        return jsonify({'response': "Invalid request"}), 400
    except Exception as e:
        app.logger.error(f"Error: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.errorhandler(500)
@cors_middleware
def internal_error(error):
    app.logger.error(f"Server Error: {str(error)}")
    return jsonify({'error': 'Internal server error'}), 500

@app.errorhandler(404)
@cors_middleware
def not_found_error(error):
    return jsonify({'error': 'Not found'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
