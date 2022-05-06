Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import sqlite3
connection = sqlite3.connect("C:/Users/Eric Tashji/Desktop/test_database.db")
c = connection.cursor()
c.execute("CREATE TABLE People(FirstName TEXT, LastName TEXT, Age INT)")
<sqlite3.Cursor object at 0x0000022862BE8540>
C.EXECUTE("INSERT INTO People VALUES ('Ron', 'Obvious', 42)")
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    C.EXECUTE("INSERT INTO People VALUES ('Ron', 'Obvious', 42)")
NameError: name 'C' is not defined. Did you mean: 'c'?
c.execute("INSERT INTO People VALUES ('Ron', 'Obvious', 42)")
<sqlite3.Cursor object at 0x0000022862BE8540>
connection = sqlite3.connect(':memory:')
c.execute("DROP TABLE IF EXISTS People")
<sqlite3.Cursor object at 0x0000022862BE8540>
connection.close()
with sqlite4.connect("test_database.db") as connection:
    