""" ******** reverse string without slicing **********"""
def reverse(s):  
    n = len(s) 
    li = list(s)    
    for i in range(n//2): 
        li[i], li[n-i-1] = li[n-i-1], li[i]
    return "".join(li)

""" ******** reverse string with slicing **********"""
inp = input("Enter String: ")
print(reverse(inp))
inp = 'CODINGAL'
print(inp[:3])
print(inp[3:])
print(inp[1:5:2])
print(inp[::-1])
print(inp[-1:-9:-2])
print(inp[-2:-9:-2])
