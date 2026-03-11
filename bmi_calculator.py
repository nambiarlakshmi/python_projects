"""Write a Python program that takes height and weight as an input from the user, calculates BMI and, 
based on the value of BMI, displays the resultant category in which the user falls."""

""""
Underweight → BMI ≤ 18.4

Healthy → BMI 18.5 to 24.9

Overweight → BMI 25.0 to 29.9

Severely Overweight → BMI 30.0 to 34.9

Obese → BMI 35.0 to 39.9

Severely Obese → BMI ≥ 40.0"""

weight = float(input("Enter your weight: "))
height = float(input("Enter your height: "))
bmi = weight / (height / 100) ** 2

if (bmi <= 18.4):
    print("You are underweight")
elif (bmi <= 24.9):
    print("You are healthy")
elif (bmi <= 29.9):
    print("You are overweight")
elif (bmi <= 34.9):
    print("You are severely overweight")
elif (bmi <= 39.9):
    print("You are obese")
else:
    print("You are severely obese")