import pymysql as PyMySQL


def open_connection():
    db = PyMySQL.connect("localhost", "root", "", "edubot")
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
    sql = "INSERT INTO noteshistory (id, title, text, time, status) VALUES (" + str(
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
        print("\n")
        d = dict()
        keys=['id','title','text','time','status']
        print([dict(zip(keys, row)) for row in result])
        db.commit()
    except:
        db.rollback()
    close_connection(db)


def select_note(db, cursor, id):
    sql = "SELECT * FROM noteshistory WHERE id=" + str(id)
    try:
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
        d = dict()
        keys = ['id', 'title', 'text', 'time', 'status']
        print([dict(zip(keys, row)) for row in result])
        db.commit()
    except:
        db.rollback()


def update_record(id, new_text):
    db = open_connection()
    cursor = db.cursor()
    sql = "UPDATE noteshistory SET text='" + new_text + "' WHERE id=" + str(id)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    close_connection(db)


if __name__ == "__main__":
    select_all_notes()
