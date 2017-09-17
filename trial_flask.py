from flask import Flask
from flask import jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Hello World"


@app.route('/chat')
def return_chat():
    chat_response = {
        'time': 12345678,
        'message': "Hello there!"
    }
    return jsonify(chat_response)
