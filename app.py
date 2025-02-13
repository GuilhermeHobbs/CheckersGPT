from flask import Flask, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
# Enable CORS for all routes
CORS(app)

@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify({
        'message': 'Hello from Railway!',
        'data': [1, 2, 3, 4, 5]
    })

if __name__ == '__main__':
    # Get port from environment variable (Railway sets this automatically)
    port = int(os.environ.get('PORT', 5000))
    # Run the app
    app.run(host='0.0.0.0', port=port)
