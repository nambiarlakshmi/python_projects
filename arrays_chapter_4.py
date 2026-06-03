""" Kadane  """
# Program to find max subarray sum
 
def maxSubArraySum(a,a_size):
    
    max =  -99999999999
    cmax = 0
    
    # Add current element to current max, check if cmax > max if yes update max, if cmax is less than 0 then reset it to 0
    for i in range(0, a_size):
        cmax = cmax + a[i]
        if (max < cmax):
            max = cmax
 
        if cmax < 0:
            cmax = 0
    return max
 
a = [1,2,3,-4,5,-22,-4,25,2,-9]
print(maxSubArraySum(a,len(a)))

""" MaxCircular """
# Standard Kadane's algorithm to find maximum subarray sum
def kadane(a):
    n = len(a)
    max_so_far = 0
    max_ending_here = 0
    for i in range(0, n):
        max_ending_here = max_ending_here + a[i]
        if (max_ending_here < 0):
            max_ending_here = 0
        if (max_so_far < max_ending_here):
            max_so_far = max_ending_here
    return max_so_far
 
# The function returns maximum circular contiguous sum in
# a[]
def maxCircularSum(a):
 
    n = len(a)
 
    # apply kadane algo if no circular is needed
    max_kadane = kadane(a)
 
    # Find sum of all element and invert them
    max_wrap = 0
    for i in range(0, n):
        max_wrap += a[i]
        a[i] = -a[i]
 
    # Apply kedance algo to find minimun inverted subarray
    max_wrap = max_wrap + kadane(a)
 
    # The maximum circular sum will be a maximum of two sums
    if max_wrap > max_kadane:
        return max_wrap
    else:
        return max_kadane
 
 
a = [11, 10, -20, 5, -3, -5, 8, -13, 10]
print("Maximum circular sum is", maxCircularSum(a))
 
