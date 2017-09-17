from apscheduler.schedulers.background import BackgroundScheduler
import time
import datetime

from mail_sender import *
from sms_sender import *

scheduler = BackgroundScheduler()


# given end time, schedule reminders
def schedule_reminders(note_id, date):
    due_timestamp = time.mktime(datetime.datetime.strptime(date, "%Y:%m:%d %H:%M:%S").timetuple())

    # if the event is due less than a day away, send an immediate reminder
    difference = due_timestamp - time.time()
    if difference < 86400:
        send_email(note_id)
        send_message('Hey, you have an assignment due today. Mind completing it?')
    elif difference < 604800:
        scheduler.add_job(send_email, 'interval', seconds=10,
                          next_run_time=datetime.datetime.fromtimestamp(time.time() + 10), args=[note_id])
    elif difference < 1209600:
        scheduler.add_job(send_email, 'interval', seconds=10,
                          next_run_time=datetime.datetime.fromtimestamp(time.time() + 10), args=[note_id])
