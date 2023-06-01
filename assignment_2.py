# Question 1
# Given an integer array nums of 2n integers, group these integers into n pairs (a1, b1), (a2, b2),..., (an, bn)
# such that the sum of min(ai, bi) for all i is maximized. Return the maximized sum.


class Solution:
    def arrayPairSum(self, nums: list[int]) -> int:
        nums.sort()
        r=0
        for i in range(0,len(nums),2):
            r+=min(nums[i],nums[i+1])
        return(r)


#Question 2
# Alice has n candies, where the ith candy is of type candyType[i].
# Alice noticed that she started to gain weight, so she visited a doctor.
# The doctor advised Alice to only eat n / 2 of the candies she has (n is always even).
# Alice likes her candies very much, and she wants to eat the maximum number of different
# types of candies while still following the doctor's advice.
# Given the integer array candyType of length n, return the maximum number of different types
# of candies she can eat if she only eats n / 2 of them.


    def dist_candies(self, candyType: list[int]) -> int:
        return min(len(candyType) >>1, len(set(candyType)))



#Question 3
# We define a harmonious array as an array where the difference between its maximum value
# and its minimum value is exactly 1.
# Given an integer array nums, return the length of its longest harmonious subsequence
# among all its possible subsequences.
# A subsequence of an array is a sequence that can be derived from the array by deleting
# some or no elements without changing the order of the remaining elements.

    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numsLen, result = len(nums), 0
        counts = {}
        for val in nums:
            if val in counts:
                counts[val] += 1
            else:
                counts[val] = 1
            inc = val + 1
            dec = val - 1
            if dec in counts:
                result = max(result, counts[val] + counts[dec])
            if inc in counts:
                result = max(result, counts[val] + counts[inc])
        return result


  # Question 4
  # You have a long flowerbed in which some of the plots are planted, and some are not.
    # However, flowers cannot be planted in adjacent plots.
    # Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty,
    # and an integer n, return true if n new flowers can be planted in the flowerbed without violating the
    # no-adjacent-flowers rule and false otherwise

    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        for i, flower in enumerate(flowerbed):
          if flower == 0 and (i == 0 or flowerbed[i - 1] == 0) and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0):
            flowerbed[i] = 1
            n -= 1
          if n <= 0:
            return True  # TC= O(n), SC = O(1)

        return False



    # Question 5
    # Given an integer array nums, find three numbers whose product is maximum and return the maximum product.

    def maximumProduct(self, nums):
        nums.sort()
        if nums[0]<0 and nums[1]<0 and abs(nums[1])>=nums[-2]:
            res=nums[0]*nums[1]*nums[-1]
        else:
            res=nums[-1]*nums[-2]*nums[-3]
        return res




    # Question 6
    # Given an array of integers nums which is sorted in ascending order, and an integer target,
    # write a function to search target in nums. If target exists, then return its index. Otherwise,
    # return -1.

    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1

        return -1



    # Question 7
    # An array is monotonic if it is either monotone increasing or monotone decreasing.
    #
    # An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is
    # monotone decreasing if for all i <= j, nums[i] >= nums[j].
    #
    # Given an integer array nums, return true if the given array is monotonic, or false otherwise

    def check_monotonic(self, array):
        return (
            # First check for decreasing order sequence...
                all(element <= array[index - 1] for index, element in enumerate(array) if index > 0) or
                # Then check for increasing order sequence...
                all(element >= array[index - 1] for index, element in enumerate(array) if index > 0)
        )




