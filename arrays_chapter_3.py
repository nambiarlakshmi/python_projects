""" Maximum1's"""

# Program to find the maximum consecutive ones in an array of 1's and 0's.
 
# Returns the result
def getMaxLength(a, a_size):
 
    counter = 0
    maxOnes = 0
 
    for i in range(0, a_size):
    
        # If we find a 0 then reset the counter
        if (a[i] == 0):
            counter = 0
 
        # If we find 1 then increment our counter and update the maxOnes
        else:
            # increase count
            counter += 1
            maxOnes = max(maxOnes, counter)
        
    return maxOnes
 
a = [1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1]
a_size = len(a)
 
print("Max 1's : ",getMaxLength(a, a_size))


"""Movesall0's """
# Program to move the 0's to the end
 
def pushZerosToEnd(a, a_size):
 
    # Zero will hold the position where non zero numbers should be
    zero = 0
 
    # Non zero will iterate to find if the current number is zero or non zero
    nonzero = 0
 
    while(nonzero!=a_size):
        if a[nonzero]!=0:
            a[nonzero],a[zero] = a[zero],a[nonzero]
            zero+=1
        nonzero+=1
        
# Driver code
a = [1,0,3,6,0,0,0,2,355,0,72]
a_size = len(a)
print(a)
pushZerosToEnd(a, a_size)
print("Array after pushing all zeros to end of array:")
print(a)

"""# Program to find the amount of water that we can trap within a given set of bars.
""" 
def findWater(a, a_size):
    # Make array to hold the height of left tallest bar for any ith bar
    leftTallest = [0]*a_size
    # Make array to hold the height of the right tallest bar for any ith bar
    rightTallest = [0]*a_size
    # Initialize result
    water = 0
    # Fill left array
    leftTallest[0] = a[0]
    for i in range( 1, a_size):
        leftTallest[i] = max(leftTallest[i-1], a[i])
    # Fill right array
    rightTallest[a_size-1] = a[a_size-1]
    for i in range(a_size-2, -1, -1):
        rightTallest[i] = max(rightTallest[i + 1], a[i])
    # Water trapped for any ith bar should be minimun of the left and right highest bar - bar height
    for i in range(0, a_size):
        water += min(leftTallest[i], rightTallest[i]) - a[i]
    return water
a = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
bars = len(a)
print("Water : ", findWater(a, bars))

"""# Program to find the max profit you can get from buying and selling stocks. You are given an array with stocks price for seven days, and you can buy and sell any day. """
 
def calculateProfits(arr,arr_size):
 
    profit = 0
    for i in range(1, arr_size):
 
        # If the current element is greater than last element then we will but the previous day and sell it the current day.
        if arr[i] > arr[i-1]:
 
            # calculate profit
            profit += arr[i] - arr[i-1]
 
    return profit
 
# Prices for 7 days
prices = [635,864,247,325,257,745,245]
 
profit = calculateProfits(prices, len(prices))
print("Max profit : ",profit)

