def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def multi(x,y):
    return x*y
def div(x,y):
    return x/y
def square(x,y):
    return x ** 2, y ** 2

x = int(input("Choose a number."))
y = int(input("Choose a number."))

print(add(x,y), sub(x,y), multi(x,y), div(x,y), square(x,y))