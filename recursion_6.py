"""     Climb stairs """

def ways(stairs):
    if stairs<0:
        return 0
    if stairs==0:
        return 1
    twoSteps=0
    oneStep=0
 
    if (stairs>=2):
        twoSteps = ways(stairs-2)
    oneStep = ways(stairs-1)
    return twoSteps+oneStep

stairs = int(input("Enter number of steps : "))
print("Number to ways to climb : ",ways(stairs))


"""Balanced parentheses """
 
def paren(s,l,r,p,n):
    if(p==2*n):
        for ss in s:
            print(ss,end='')
        print("\n")
        return
    if(l>r):
        s[p]="}"
        paren(s,l,r+1,p+1,n)
    if(l<n):
        s[p]="{"
        paren(s,l+1,r,p+1,n)
 
 
n = int(input("Enter number of parenthesis : "))
s = [""]*2*n
print("\n")
paren(s,0,0,0,n)
