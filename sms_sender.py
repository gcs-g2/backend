from twilio.rest import Client

account = 'AC8f8831388e1aa533e044789ea82beacd'
token = '38c5a51c95aed49aeaf92a334bea0059'
client = Client(account, token)


def send_message(body):
    message = client.messages.create(to="+14696189426", from_="+16672399780", body=body)
