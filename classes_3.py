
"""Write a program to create a class Parrot and perform the following tasks - Create a class variable species 
Create a __init__ method that has instance variables - name and age Create instances of class Parrot, passing 
arguments as well Print Class variable by accessing it Print Instance variables as well"""

class Parrot:
    species =" Bird"
    def __init__(self, name, age):
        self.name = name
        self.age = age

pink = Parrot("Emma", 23)
red = Parrot("Keller", 13)

print(f"{pink.name} is {pink.age}")
print(f"{red.name} is {red.age}")