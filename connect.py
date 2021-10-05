import sqlite3
def create_table(dbname):
        conn = sqlite3.connect(dbname)
        conn.execute("CREATE TABLE IF NOT EXISTS FLIPFLOP (NAME TEXT,PRICE INT,ORIGINALPRICE INT)")
        print("table created successfully!!")
        conn.close()
def insert_into_table(dbname,values):
        conn = sqlite3.connect(dbname)
        conn.execute("INSERT INTO FLIPFLOP (NAME,PRICE,ORIGINALPRICE) VALUES (?,?,?)",values)
        conn.commit()
        conn.close()

def get_the_info(dbname):
        conn = sqlite3.connect(dbname)
        cur = conn.cursor()
        cur.execute("SELECT * FROM FLIPFLOP")
        data=cur.fetchall()
        for record in data:
            print(record)
