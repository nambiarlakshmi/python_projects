"""Write a program to create a class with name Student and perform the following tasks - Create a class variable 
grade and name Create a function to print a sentence Create a function to print class variables grade and name 
Create an object of class Student Call the two functions to execute them"""

class Student:
    grade = 7
    name = 'Lakshmi'
    
    def camel(self):
        print(self.grade, self.name)
    
tomato = Student()
tomato.camel()
    