# 1. O(n^2) time | O(1) space
def twoNumberSum(array, targetSum):
    for i in range(len(array) - 1):
        first_num = array[i]
        for j in range(i + 1, len(array)):
            second_num = array[j]
            if first_num + second_num == targetSum:
                return [first_num, second_num]
    return []

# O(n) time | O(n) space
def twoNumberSum(array, targetSum):
    nums = {}
    for num in array:
        potential_match = targetSum - num
        if potential_match in nums:
            return [potential_match, num]
        else:
            nums[num] = True
    return []

# O(nLog(n)) | O(1) space
def twoNumberSum(array, targetSum):
    array.sort()
    left, right = 0, len(array) - 1
    while left < right:
        current_sum = array[left] + array[right]
        if current_sum == targetSum:
            return [array[left], array[right]]
        elif current_sum < targetSum:
            left += 1
        elif current_sum > targetSum:
            right -= 1
    return []