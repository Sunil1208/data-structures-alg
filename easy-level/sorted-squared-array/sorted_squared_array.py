# SORTED SQUARED ARRAY

# Write a function that takes in a non-empty array of integers that are sorted iin ascending order 
# and returns a new array of the same length with the squares of the original integers also sorted in ascending order.

# Sample Input

# array = [1, 2, 3, 5, 6, 8, 9]

# Sample Output

# [1, 4, 9, 25, 36, 64, 81]

# O(nLogn) time | O(n) space
def sortedSquaredArray(array):
    sorted_squares = [0 for _ in array]
    for idx in range(len(array)):
        value = array[idx]
        sorted_squares[idx] = value * value
    sorted_squares.sort()
    return sorted_squares

def sortedSquaredArray(array):
    sorted_squares = [0 for _ in array]
    smaller_value_idx, larger_value_idx = 0, len(array) - 1
    for idx in reversed(range(len(array))):
        smaller_value = array[smaller_value_idx]
        larger_value = array[larger_value_idx]

        if abs(smaller_value) > abs(larger_value):
            sorted_squares[idx] = smaller_value * smaller_value
            smaller_value_idx += 1
        else:
            sorted_squares[idx] = larger_value * larger_value
            larger_value_idx -= 1
    return sorted_squares