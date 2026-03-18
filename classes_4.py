"""Write a program to create a class Parrot and perform the following tasks - Create a class variable species
 Create a constructor that has instance variables - name and age Create instance methods for this class named
sing and dance, making them print a message. Create instances of class Parrot, passing arguments as well Print
 Class variable by accessing it Print Instance variables as well"""

class Parrot:
    species =" Bird"
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def sing(self, song):
        return f"{self.name} sings {song}"
    def dance(self):
        return f"{self.name} is dancing."
red = Parrot("Keller", 13)
print(red.sing("Happy Birthday"))
print(red.dance())
