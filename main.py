# External packages
from flask import Flask
from flask import request
import jsonpickle

# Importing files
from chat import *
from notes import *

app = Flask(__name__)


# allow cross origin requests
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response


@app.route('/')
def handle_default():
    return 'Try either /chat or /note'


@app.route('/chat', methods=['GET', 'POST', 'PUT'])
def handle_chat():
    if request.method == 'GET':
        return jsonpickle.encode(get_chat())

    if request.method == 'POST':
        return jsonpickle.encode(save_chat())

    if request.method == 'PUT':
        return jsonpickle.encode(save_chat())


@app.route('/notes')
def return_all_notes():
    return jsonpickle.encode(get_all_notes())


@app.route('/note/<note_id>')
def get_single_note(note_id):
    return jsonpickle.encode(get_note(note_id))


@app.route('/note', methods=['POST'])
def handle_note_create():
    data = jsonpickle.decode(request.data)
    return jsonpickle.encode(create_note(data))


@app.route('/note/<note_id>', methods=['PUT'])
def handle_note_update(note_id):
    data = jsonpickle.decode(request.data)
    return jsonpickle.encode(update_note(data))


if __name__ == "__main__":
    app.run()
