# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

# Example 1
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2
# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list(int):
        hash_map = {}
        for idx, item in enumerate(nums):
            potential_match = target - item
            if potential_match in hash_map:
                return [hash_map[potential_match], idx]
            else:
                hash_map[item] = idx
        return []
    
nums = [2,7,11,15]
target = 9
my_solution = Solution()
print(my_solution.twoSum(nums, target))