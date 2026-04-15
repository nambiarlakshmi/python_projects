""" Time complexity O(1)"""
def printnumber(n):
  iteration=0
  print("The number entered by user is ",n)
  iteration+=1
  print("Total iterations done by the code is ",iteration,"\n")
printnumber(10)
printnumber(20)
print("\n With any 'n' the time taken by our code won't change")

"""Time Complexity = O(n)"""
def OnTime(n):
  iteration=0 
  for i in range(1,n+1): 
    iteration+=1 
  print("When n is ",n," Iterations = ",iteration)
OnTime(10)
OnTime(20)
OnTime(42)
print("\nWith every 'n' the time taken and iterations will increase")

"""Time Complexity = O(n^2)"""
def ONSquareTime(n):
  iteration=0     O(1)
  for i in range(0,n): O(n)
    for j in range(0,n):O(n) 
      print("*", end =" ") O(1)
      iteration+=1 O(1)
    print("") O(n)
  print("\nWhen n is ",n," Iterations = ",iteration,"\n")O(1)

 
ONSquareTime(5)
ONSquareTime(4)
ONSquareTime(3)
 
print("\nWith every 'n' the time taken equals n^2")
print("O(n^2)")