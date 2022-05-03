class User: #This creates the parent class with various objects
    name = 'Eric Tashji'
    email = 'etashji@gmail.com'
    password = 'password'
    account_number = 0

class Employee(User): #This creates a child class that inherits from the parent class
    base_pay = 200.00
    department = 'General'

class Customer(User): #This creates another child class that inherits from the parent class
    mailing_adddress = '123 Address Street, Hot Place, New Mexico'
    mailing_list = True
    
    
