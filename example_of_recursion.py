"""
Tail recrursion 
Head Recursion 
Tree Recrusion 

********* Tail Recrusion **********
def tail(n):
    if (n!=0):
        print(n)
        # Recursive call is last statement of function
        tail(n - 1)
x = 4
tail(x)

********* Head  Recrusion **********
def head(n):
    if (n!=0):
        head(n - 1)
        print(n)
x = 5
head(x)

********* Tree  Recrusion **********
def tree(n):
    if (n != 0):
        print(n)
        tree(n - 1)
        tree(n - 1)
tree(2)
"""

