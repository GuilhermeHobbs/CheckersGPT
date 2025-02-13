from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)

# Configure CORS with specific origins
CORS(app, resources={
    r"/ask-name": {
        "origins": [
            "https://guilhermehobbs.github.io",
            "http://localhost:5000"  # For local testing
        ],
        "methods": ["GET"],
        "allow_headers": ["Content-Type"]
    }
})

@app.route('/ask-name')
def ask_name():
    # Get the question parameter from the URL
    question = request.args.get('question', '')
    
    # Check if the received question is correct
    if question == "The Name?":
        return {"answer": "It's me"}
    else:
        return {"answer": "Invalid question"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
