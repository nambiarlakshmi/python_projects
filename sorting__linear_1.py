"""
UnderstandinGLinearSearch
# Program for searching an element using Linear Search 
"""

# Function to search for an element
def search(arr, n, x):
    for i in range(0, n):
        if (arr[i] == x):
            return i

    # if element is not found in the array
    # return -1
    return -1

# Take array input from user
# Enter element to search for
arr = [2, 3, 4, 10, 40]
x = 10
n = len(arr)

# Function call
result = search(arr, n, x)
# check returned index and print the output
if(result == -1):
    print("Element is not present in array")
else:
    print("Element is present at index", result)

"""
FindingDuplicates
# Search list and target value
"""
tour_locations = [ "New York City", "Los Angeles", "Bangkok", "Istanbul", "London", "New York City", "Toronto" ]
target_city = "New York City"

#Linear Search Algorithm
def linear_search(search_list, target_value):
    matches = []
    for idx in range(len(search_list)):
        if search_list[idx] == target_value:
            # If target value found in the list
            # add index in matches list
            matches.append(idx)

    # If the element is not in matches list
    # Raise an error
    if not matches:
        raise ValueError("{} is not in the list".format(target_value))
    # Otherwise return the matches list
    # with indexes where element is present
    else:
        return matches

#Function call
tour_stops = linear_search(tour_locations, target_city)
print("{} is present in following locations in the list: {}".format(target_city,tour_stops))