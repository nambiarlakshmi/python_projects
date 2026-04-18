""" ********** Head Recursion **********"""
def headrec(n, num):
    if n > num:
        return
    headrec(n + 1, num)
    print(n)

n = int(input("Enter n to print 1 to n: "))
headrec(1, n)

""" ********** Tail Recursion **********"""
def tailrec(n, num):
    if n > num:
        return
    print(n)
    tailrec(n + 1, num)

n = int(input("Enter n to print 1 to n: "))
tailrec(1, n)

""" ********** Linear Recursion **********"""
def incdec(n,num):
    if(n<1 or n>num):
        return
    print(n)
    incdec(n-1,num)
    print(n)
 
n = int(input("Enter any number n : "))
incdec(n,n)

"""
5
↓
4
↓
3
↓
2
↓
1
"""

""" ********** Tree Recursion **********"""
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
print(fib(5))

"""       5
       /     \
      4       3
     /  \     / \
    3    2   2   1
   / \  / \
  2  1 1  0                """