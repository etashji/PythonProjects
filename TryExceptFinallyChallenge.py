def getNumbers():
    var1 = input("What is the first number? ")
    var2 = input("What is your second number? ")
    add(var1, var2)

def add(var1,var2):
    var3 = int(var1) + int(var2)
    print("{} + {} = {}".format(var1,var2,var3))

getNumbers()
