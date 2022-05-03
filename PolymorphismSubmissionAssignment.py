class User:
    username = "Username"
    password = "password"

    def login(self):
        entry_username = input("Enter your username: ")
        entry_password = input("Enter your password: ")
        if (entry_username == self.username and entry_password == self.password):
            print("Hello, {}!".format(self.username))
        else:
            print("Intruder alert! Red spy is in the base!")

class UserV2(User):
    email = "email@email.com"
    pin = "12345"

    def login(self):
        entry_email = input("Enter your email: ")
        entry_pin = input("Enter your pin: ")
        if (entry_email == self.email and entry_pin == self.pin):
            print("Hello!")
        else:
            print("Intruder alert! Red spy is in the base!")

class UserV3(User):
    name = "Name"
    passphrase = "passphrase"

    def login(self):
        entry_name = input("Enter your name: ")
        entry_passphrase = input("Enter your passphrase: ")
        if (entry_name == self.name and entry_passphrase == self.passphrase):
            print("Hello, {}!".format(self.name))
        else:
            print("Intruder alert! Red spy is in the base!")

user1 = User()
user1.login()

user2 = UserV2()
user2.login()

user3 = UserV3()
user3.login()
