def get_note(note_id):
    return {
        "id": note_id,
        "title": 'Artificial Intelligence',
        "text": 'Artificial Intelligence is very very important',
        "date": '',
        "status": 'pending'
    }


def get_all_notes():
    return [
        {
            "id": 1,
            "title": 'Artificial Intelligence',
            "text": 'Artificial Intelligence is very very important',
            "date": '',
            "status": 'pending'
        },
        {
            "id": 2,
            "title": 'DAA',
            "text": 'DAA is the most important',
            "date": '',
            "status": 'pending'
        },
        {
            "id": 3,
            "title": 'DBMS',
            "text": 'DBMS can be flunked!',
            "date": '',
            "status": 'pending'
        }
    ]

def update_note(data):
    return data


def create_note(data):
    return data
