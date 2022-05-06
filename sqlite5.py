import sqlite3

firstName = input("Enter your first name: ")
lastName = input("Enter your last name: ")
age = int(input("Enter your age: "))

with sqlite3.connect('test_database.db') as connection:
    c = connection.cursor()
    line = "INSERT INTO People VALUES ('" + firstName +"', '"+ lastName"', " +str(age) +")"
    c.execute(line)

