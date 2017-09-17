from flask import Flask
from flask import jsonify
from flask import request
from chat import *

app = Flask(__name__)

@app.route('/')
def handle_default():
    return 'Try either /chat or /note'

@app.route('/chat', methods=['GET', 'POST', 'PUT'])
def handle_chat():
    if request.method == 'GET':
        return jsonify(get_chat())

    if request.method == 'POST':
        return jsonify(save_chat())

    if request.method == 'PUT':
        return jsonify(save_chat())


if __name__ == "__main__":
    app.run()

