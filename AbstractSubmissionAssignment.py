from abc import ABC, abstractmethod #This imports the code required to make abstract classes.
class abstract(ABC): # This is our abstract class.
    @abstractmethod # This indicates that our next method is abstract
    def abstractMethod(self, amount): #This is our abstract method
        pass #This passes the method so there is not value for amount.
 
    def regularMethod(self): #This is my regular method.
        print("This is my regular method.") # This prints the string for the method.

class regular(abstract): # This is my regular class
    def abstractMethod(self, amount): #This redefines the abstractmethod from above.
        print("This is the amount of my abstract method: {}.".format(amount)) #This prints the info for the abstractmethod.

obj = regular() #This creates an object.
obj.regularMethod() #This implements the regular method for the object.
obj.abstractMethod("100") #This prints the abstract method for the object.
