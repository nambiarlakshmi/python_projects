"""
UnderstandingBinary Search
# Program to implement iterative Binary Search.
"""

# Function to return the index if element is found
def binarySearch(arr, l, r, x):
    while l <= r:
        mid = l + (r - l) // 2

        # Check if x is present at mid
        if arr[mid] == x:
            return mid

        # If x is greater, ignore left half
        elif arr[mid] < x:
            l = mid + 1

        # If x is smaller, ignore right half
        else:
            r = mid - 1

    # return -1 if element isn't found
    return -1

# Driver Code
arr = [2, 3, 4, 10, 40]
x = 10

# Function call
result = binarySearch(arr, 0, len(arr) - 1, x)

if result != -1:
    print("Element {} is present at index {}".format(x, result))
else:
    print("Element is not present in array")
    
"""Recursive Binary Search"""
# Program to perform binary search recursively
def binarySearch(arr, l, r, x):
    # Check if the length of array is greater than or equal to 0
    if r >= l:
        # find the mid element's index
        mid = l + (r - l) // 2

        # If element is present at the middle itself
        if arr[mid] == x:
            return mid

        # If element is smaller check in left subarray
        elif arr[mid] > x:
            return binarySearch(arr, l, mid-1, x)

        # Else check in right subarray
        else:
            return binarySearch(arr, mid + 1, r, x)
    else:
        # Element is not present in the array
        return -1

# Driver Code
arr = [2, 3, 4, 10, 40]
x = 10

# Function call
result = binarySearch(arr, 0, len(arr)-1, x)

if result != -1:
    print("Element {} is present at index {}".format(x, result))
else:
    print("Element is not present in array")
    

"""SmallestMissingElement """
# Function to find the smallest missing element in a sorted
# list of distinct non-negative integers
def findSmallestMissing(nums, left=None, right=None):
    # initialize left and right
    if left is None and right is None:
        (left, right) = (0, len(nums) - 1)

    # base condition
    if left > right:
        return left

    mid = left + (right - left) // 2

    # if the mid-index matches with its value, then the mismatch
    # lies on the right half
    if nums[mid] == mid:
        return findSmallestMissing(nums, mid + 1, right)

    # mismatch lies on the left half
    else:
        return findSmallestMissing(nums, left, mid - 1)

if __name__ == '__main__':
    nums = [0, 1, 2, 6, 9, 11, 15]

    print('The smallest missing element is', findSmallestMissing(nums))