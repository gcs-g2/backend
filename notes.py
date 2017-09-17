from reminder_scheduler import *
from database import *


def get_note(note_id):
    return {
        "id": note_id,
        "title": 'Artificial Intelligence',
        "text": 'Artificial Intelligence is very very important',
        "date": '',
        "status": 'pending'
    }


def get_all_notes():
    return select_all_notes()


def update_note(data):
    return data


def create_note(data):
    schedule_reminders(0, data['date'])
    insert_into_note_list(data['title'], data['text'], data['date'], data['status'])
    return data
