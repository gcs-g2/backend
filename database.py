import pymysql as PyMySQL


def open_connection():
    db = PyMySQL.connect("localhost", "root", "mysql", "edubot")
    return db


def close_connection(db):
    db.close()
    print("db connection closed")


def getID(db, cursor):
    num = 0
    sql = "SELECT max(id) FROM noteshistory"
    id = 0
    try:
        cursor.execute(sql)
        num = cursor.fetchone()
        id = num[0] + 1
        db.commit()
    except:
        db.rollback()
    return id


def insert_into_note_list():
    db = open_connection()
    cursor = db.cursor()
    id = getID(db, cursor)
    sql = "INSERT INTO noteshistory (id, title, note_text, time, status) VALUES (" + str(
        id) + ",'artificial intelligence','assignment is due','4:5:6','pending')"
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    close_connection(db)


def select_all_notes():
    db = open_connection()
    cursor = db.cursor()
    sql = "SELECT * FROM noteshistory"
    try:
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
        db.commit()
    except:
        db.rollback()
    close_connection(db)


def update_record(id, new_text):
    db = open_connection()
    cursor = db.cursor()
    sql = "UPDATE noteshistory SET note_text='" + new_text + "' WHERE id=" + str(id)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    close_connection(db)
