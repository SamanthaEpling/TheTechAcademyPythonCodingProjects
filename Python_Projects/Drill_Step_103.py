import sqlite3

conn = sqlite3.connect('step103.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files(\
        ID INTEGER PRIMARY KEY AUTOINCREMENT, col_ftypes TEXT)")
    conn.commit()
conn.close()


conn = sqlite3.connect('step103.db')

with conn:
    cur = conn.cursor()
    cur.execute("INSERT INTO tbl_files(col_ftypes) VALUES ('information.docx')")
    cur.execute("INSERT INTO tbl_files(col_ftypes) VALUES ('Hello.txt')")
    cur.execute("INSERT INTO tbl_files(col_ftypes) VALUES ('myImage.png')")
    cur.execute("INSERT INTO tbl_files(col_ftypes) VALUES ('myMovie.mpg')")
    cur.execute("INSERT INTO tbl_files(col_ftypes) VALUES ('World.txt')")
    cur.execute("INSERT INTO tbl_files(col_ftypes) VALUES ('data.pdf')")
    cur.execute("INSERT INTO tbl_files(col_ftypes) VALUES ('myPhoto.jpg')")
    conn.commit()
conn.close()


conn = sqlite3.connect('step103.db')

with conn:
    cur = conn.cursor()
    cur.execute("SELECT col_ftypes FROM tbl_files WHERE col_ftypes LIKE '%.txt'")
    varTextFiles = cur.fetchall()
    for item in varTextFiles:
        msg = "{} is a text file.".format(item)
        print(msg)
conn.close()
