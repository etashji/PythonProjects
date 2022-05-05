class Protected: 
    def __init__(self):
        self.__privateVar = 12 # This creates a private variable
        self.__protectedVar = 13

    def getPrivate(self):
        print(self.__privateVar)

    def setPrivate(self, private):
        self.__privateVar = private

    def setProtected(self, protected):
        self.__protectedVar = protected

    def getProtected(self):
        print(self.__protectedVar)

obj = Protected()
obj.setPrivate(23)
obj.getPrivate()
obj.setProtected(12)
obj.getProtected()
