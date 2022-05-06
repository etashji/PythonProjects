Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import sqlite3
with sqlite4.connect('test_database.db') as connection:
    c = connection.cursor()
    c.executescript("""DROP TABLE IF EXISTS People;
                    CREATE TABLE People(FirstName TEXT, LastName TEXT, Age INT);
                    INSERT INTO People VALUES ('Ron', 'Obvious', '42');
                    """)

    
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    with sqlite4.connect('test_database.db') as connection:
NameError: name 'sqlite4' is not defined. Did you mean: 'sqlite3'?
with sqlite3.connect('test_database.db') as connection:
    c = connection.cursor()
    c.executescript("""DROP TABLE IF EXISTS People;
                    CREATE TABLE People(FirstName TEXT, LastName TEXT, Age INT);
                    INSERT INTO People VALUES ('Ron', 'Obvious', '42');
                    """)

    
<sqlite3.Cursor object at 0x0000027FBE1C85C0>
peopleValues = (('Luigi', 'Vercotti', 43), ('Arthur', 'Belling', 28))
c.executemany("INSERT INTO People VALUES(?,?,?)", peopleValues)
<sqlite3.Cursor object at 0x0000027FBE1C85C0>
