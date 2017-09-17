# External packages
from flask import Flask
from flask import request
import jsonpickle

# Importing files
from chat import *
from notes import *

app = Flask(__name__)

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

@app.route('/note', methods=['POST', 'PUT'])
def handle_note_update_or_create():
    data = jsonpickle.decode(request.data)

    if data['id']:
        return jsonpickle.encode(update_note(data))
    else:
        return jsonpickle.encode(create_note(data))


if __name__ == "__main__":
    app.run()

