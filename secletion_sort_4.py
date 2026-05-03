# program for Selection Sort
A = [64, 25, 12, 22, 11]

# Traverse through the array
for i in range(len(A)):

    # Find the minimum element in remaining array
    min_id = i
    for j in range(i+1, len(A)):
        if A[min_id] > A[j]:
            min_id = j

    # Swap the found minimum element with
    # the first element
    A[i], A[min_id] = A[min_id], A[i]

# Driver code
print("Sorted array")
for i in range(len(A)):
    print("%d" %A[i],end=" ")
    

# build-in function
def compare(n1, n2):
    return str(n1) + str(n2) > str(n2) + str(n1)

# selection sort
def largestNumber3(nums):
    for i in range(len(nums), 0, -1):
        tmp = 0
        for j in range(i):
            if not compare(nums[j], nums[tmp]):
                tmp = j
        nums[tmp], nums[i-1] = nums[i-1], nums[tmp]
    return str(int("".join(map(str, nums))))

# Driver Code
arr = [3,30,34,5,9]
print("Given Array:", arr)
print("Largest Possible Number:", largestNumber3(arr))