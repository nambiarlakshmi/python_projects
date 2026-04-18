def checkSorted(a):
    length = len(a)
    if length == 1 or length == 0:
        return True
    return a[0] <= a[1] and checkSorted(a[1:])
 
a = [1,2,3,5,6,8,2]
if checkSorted(a):
    print("\nYes given array is sorted")
else:
    print("\nNo given array is not sorted")



def arrayTotalSum(a):
     length = len(a)
     if length == 1:
        return a[0]
     return a[0] + arrayTotalSum(a[1:])
a = [1,2,3,6] 
print("Array total sum: ",arrayTotalSum(a))


def MaxElementArray(a):
    length = len(a)
    if length == 1:
        return a[0]
    return max(a[0],MaxElementArray(a[1:]))

# max(value1, value2, value3, ...)

a = [1,2,234,234,745,3,6,653]
print("Largest element of array: ",MaxElementArray(a))