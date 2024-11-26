import pymysql

def insert_record(module, topic, question):
    conn = pymysql.connect(
        host = 'railgunglm-database.c5kqkuqg49fj.us-east-1.rds.amazonaws.com',
        port = 3306,
        user = 'admin',
        password = 'railgunglm-database',
        db = 'stats',
        )
    cur = conn.cursor()
    cur.execute("INSERT INTO setting (module, topic, question) VALUES (%s,%s,%s);", (module, topic, question))
    conn.commit()

def get_setting():
    conn = pymysql.connect(
        host = 'railgunglm-database.c5kqkuqg49fj.us-east-1.rds.amazonaws.com',
        port = 3306,
        user = 'admin',
        password = 'railgunglm-database',
        db = 'stats',
        )
    cur = conn.cursor()
    cur.execute("SELECT * FROM setting")
    details = cur.fetchall()
    return details

def insert_answer(question, answer):
    conn = pymysql.connect(
        host = 'railgunglm-database.c5kqkuqg49fj.us-east-1.rds.amazonaws.com',
        port = 3306,
        user = 'admin',
        password = 'railgunglm-database',
        db = 'stats',
        )
    cur = conn.cursor()
    cur.execute("INSERT INTO answer (question, answer) VALUES (%s,%s);", (question, answer))
    conn.commit()