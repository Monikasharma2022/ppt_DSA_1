
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# You can return the answer in any order

class Solution:
    def twoSum(self, nums, target):
        index_map = {}
        for index, num in enumerate(nums):
            if target - num in index_map:
                return index_map[target - num], index
            index_map[num] = index

obj = Solution()
ans = obj.twoSum([2,7,11,15,4,5,3], 14)
print(ans)