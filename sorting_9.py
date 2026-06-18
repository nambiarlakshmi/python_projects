# Find if There is a Pair in A[0..N-1] with Given Sum

# Method
def isPairSum(A, N, X):

    for i in range(N):
        for j in range(N):

            # as equal i and j means same element
            if(i == j):
                continue

            # pair exists
            if (A[i] + A[j] == X):
                return [A[i], A[j]]

            # as the array is sorted
            if (A[i] + A[j] > X):
                break

    # No pair found with given sum
    return 0

# array declaration
arr = [2, 3, 5, 8, 9, 10, 11]

# value to search
val = 17

print("Pair with the sum equal to {} is - {}".format(val, isPairSum(arr, len(arr), val)))

# Find if There is a Pair in A[0..N-1] with Given Sum
# Using Two-pointers Technique

# Method
def isPairSum(A, N, X):

    # represents first pointer
    i = 0

    # represents second pointer
    j = N - 1

    while(i < j):

        # If we find a pair
        if (A[i] + A[j] == X):
            return [A[i], A[j]]

        # If sum of elements at current
        # pointers is less, we move towards
        # higher values by doing i += 1
        elif(A[i] + A[j] < X):
            i += 1

        # If sum of elements at current
        # pointers is more, we move towards
        # lower values by doing j -= 1
        else:
            j -= 1
    return 0

# array declaration
arr = [2, 3, 5, 8, 9, 10, 11]

# value to search
val = 17

print("Pair with the sum equal to {} is - {}".format(val, isPairSum(arr, len(arr), val)))

# program to find the pair with sum
# closest to a given no.

MAX_VAL = 100000000

# Function to print the pair with sum closest to x
def printClosest(arr, n, x):

    # To store indexes of result pair
    res_l, res_r = 0, 0

    #Initialize left and right indexes
    # and difference between
    # pair sum and x
    l, r, diff = 0, n-1, MAX_VAL

    # While there are elements between l and r
    while r > l:

        # Check if this pair is closer than the
        # closest pair so far
        if abs(arr[l] + arr[r] - x) < diff:
            res_l = l
            res_r = r
            diff = abs(arr[l] + arr[r] - x)

        if arr[l] + arr[r] > x:
            # If this pair has more sum, move to
            # smaller values.
            r -= 1
        else:
            # Move to larger values
            l += 1

    print('The closest pair to sum {} is {} and {}'.format(x, arr[res_l], arr[res_r]))

# Driver code to test above
if __name__ == "__main__":
    arr = [10, 22, 28, 29, 30, 40]
    n = len(arr)
    x=54
    printClosest(arr, n, x)