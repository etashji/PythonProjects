import sqlite3

conn = sqlite3.connect('datbase.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_table (\
                ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                col_filenames TEXT)")
    conn.commit()

fileList = ('information.docx', 'Hello.txt', 'myImage.png',\
            'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')
import glob
for file in glob.glob("*.txt"):
    with conn:
        cur = conn.cursor()
        cur.execute('INSERT INTO tbl_table(col_filenames) VALUES (?)', \
                    (file,))
        conn.commit()

with conn:
    cur = conn.cursor()
    cur.execute("SELECT col_filenames FROM tbl_table")
    varFile = cur.fetchall()
    for item in varFile:
        msg = "File Name: {}".format(item[0])
    print(msg)
