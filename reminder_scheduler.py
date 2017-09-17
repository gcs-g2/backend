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
        send_message('Hey, remember logging in to Hyper Memory to revise your concepts. I will remind again soon.')

        # schedule after 6 hours
        scheduler.add_job(send_email, 'interval', seconds=10,
                          next_run_time=datetime.datetime.fromtimestamp(time.time() + 21600), args=[note_id])
    elif difference < 604800:
        scheduler.add_job(send_email, 'interval', seconds=10,
                          next_run_time=datetime.datetime.fromtimestamp(time.time() + 10), args=[note_id])

        scheduler.add_job(send_email, 'interval', seconds=10,
                          next_run_time=datetime.datetime.fromtimestamp(time.time() + (3600 * 24 * 1)), args=[note_id])
        scheduler.add_job(send_email, 'interval', seconds=10,
                          next_run_time=datetime.datetime.fromtimestamp(time.time() + (3600 * 24 * 4)), args=[note_id])
        scheduler.add_job(send_email, 'interval', seconds=10,
                          next_run_time=datetime.datetime.fromtimestamp(time.time() + (3600 * 24 * 10)), args=[note_id])
    elif difference < 1209600:
        scheduler.add_job(send_email, 'interval', seconds=10,
                          next_run_time=datetime.datetime.fromtimestamp(time.time() + 10), args=[note_id])
        scheduler.add_job(send_email, 'interval', seconds=10,
                          next_run_time=datetime.datetime.fromtimestamp(time.time() + (3600 * 24 * 3)), args=[note_id])
        scheduler.add_job(send_email, 'interval', seconds=10,
                          next_run_time=datetime.datetime.fromtimestamp(time.time() + (3600 * 24 * 7)), args=[note_id])
        scheduler.add_job(send_email, 'interval', seconds=10,
                          next_run_time=datetime.datetime.fromtimestamp(time.time() + (3600 * 24 * 14)), args=[note_id])
        scheduler.add_job(send_email, 'interval', seconds=10,
                          next_run_time=datetime.datetime.fromtimestamp(time.time() + (3600 * 24 * 21)), args=[note_id])