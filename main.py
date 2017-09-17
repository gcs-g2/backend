from flask import Flask
from flask import jsonify
from flask import request
import json
import jsonpickle

from chat import *
from notes import *

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

@app.route('/notes')
def return_all_notes():
    return jsonpickle.encode(get_all_notes())

@app.route('/note/<note_id>')
def get_single_note(note_id):
    return jsonify(get_note(note_id))

@app.route('/note', methods=['POST', 'PUT'])
def handle_note_update_or_create():
    data = json.loads(request.data)

    if data['id']:
        return jsonify(update_note(data))
    else:
        return jsonify(create_note(data))


if __name__ == "__main__":
    app.run()

