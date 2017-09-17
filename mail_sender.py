import requests

key = 'key-9af56158081243ed783b2fa3dd6bd131'
sandbox = 'mg.ishan.co'
recipient = 'ishan.sharma001@gmail.com'

request_url = 'https://api.mailgun.net/v3/{0}/messages'.format(sandbox)
def send_email(note_id):
    # for now, just print note_id
    print("Going to send email for note ID ", note_id)

    request = requests.post(request_url, auth=('api', key), data={
        'from': 'hello@mg.ishan.co',
        'to': 'ishan.sharma001@gmail.com',
        'subject': "Study Reminder!",
        'text': "You have a pending assignment for Artificial Intelligence in 1 hour"
    })

    print("Email Request Status: {0}".format(request.status_code))
    print("Email Request Body: {0}".format(request.text))
