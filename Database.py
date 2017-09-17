import pymysql as PyMySQL
import jsonpickle as JsonPickle

def open_connection():
    db = PyMySQL.connect("localhost", "root", "", "edubot")
    return db

def close_connection(db):
    var = db.close
    print(var)

def getID(table_name):
    db = open_connection()
    cursor = db.cursor()
    num=0
    sql = "SELECT max(id) FROM noteshistory"
    try:
        cursor.execute(sql)
        num=cursor.fetchone()+1
        db.commit()
    except:
        db.rollback()
    close_connection(db)
    return num

def insert_into_note_list():
    db = open_connection()
    cursor = db.cursor()
    id = getID("noteshistory")
    sql = "INSERT INTO noteshistory (id,note_text,time) VALUES (" + str(id) + ",'Hey','1:1:1')"
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    close_connection(db)

def select_all_notes():
    db = open_connection()
    cursor = db.cursor()
    sql = "select * from noteshistory"
    try:
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
        print("\n")
        print(JsonPickle.encode(result))
        db.commit()
    except:
        db.rollback()
    close_connection(db)

if __name__ == "__main__":
    insert_into_note_list()
    select_all_notes()
