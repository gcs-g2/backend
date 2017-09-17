import pymysql as PyMySQL


def open_connection():
    db = PyMySQL.connect("localhost", "root", "", "edubot")
    return db


def close_connection(db):
    var = db.close
    print("connection closed")


def getID():
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


def insert_into_note_list(db, cursor):
    id = getID()
    sql = "INSERT INTO noteshistory (id, title, note_text, time, status) VALUES (" + str(
        id) + ",'artificial intelligence','assignment is due','4:5:6','pending')"
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()


def select_all_notes(db, cursor):
    sql = "SELECT * FROM noteshistory"
    try:
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
        db.commit()
    except:
        db.rollback()


def select_note(db, cursor, id):
    sql = "SELECT * FROM noteshistory WHERE id=" + str(id)
    try:
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
        db.commit()
    except:
        db.rollback()


def update_record(id, new_text):
    sql = "UPDATE noteshistory SET note_text='" + new_text + "' WHERE id=" + str(id)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()


if __name__ == "__main__":
    db = open_connection()
    cursor = db.cursor()
    # insert_into_note_list(db, cursor)
    # select_all_notes(db, cursor)
    update_record(2, "assignment done")
    close_connection(db)
