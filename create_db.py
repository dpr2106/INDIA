import sqlite3
def create_db():
    con=sqlite3.connect(database='rms.db')
    cur=con.cursor()
    
    cur.execute("CREATE TABLE IF NOT EXISTS course(cid INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, duration TEXT, charges TEXT, description TEXT)")
    
    
    cur.execute("CREATE TABLE IF NOT EXISTS student(roll INTEGER PRIMARY KEY AUTOINCREMENT,name text,email text,gender text,dob text,contact text,admission text,course text,state text,city text,pin text,address text)")
    
    cur.execute("CREATE TABLE IF NOT EXISTS result(rid INTEGER PRIMARY KEY AUTOINCREMENT, roll TEXT,name text, course TEXT, marks_ob TEXT, full_marks TEXT,per text)")
    
    con.commit()
    con.close()


create_db()
