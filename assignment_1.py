
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order

class Solution:
    def twoSum(self, nums, target):
        index_map = {}
        for index, num in enumerate(nums):
            if target - num in index_map:
                return index_map[target - num], index
            index_map[num] = index


# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
# The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.
# Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:
# - Change the array nums such that the first k elements of nums contain the elements which are not equal to val.
# The remaining elements of nums are not important as well as the size of nums.
# - Return k.

    def removeElement(self, nums: list[int], val: int):
        # Counter for keeping track of elements other than val
        count = 0
        # Loop through all the elements of the array
        for i in range(len(nums)):
            if nums[i] != val:
                nums[count] = nums[i]
                count += 1

        return count, nums[0:count]


# Given a sorted array of distinct integers and a target value,return the index if the target is found.
# If not,return the index where it would be if it were inserted in order.You must write an algorithm with O(log n) runtime complexity.

    def searchInsert(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) >> 1
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1
        return left


# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer.
# The digits are ordered from most significant to least significant in left-to-right order.
# The large integer does not contain any leading 0's.
# Increment the large integer by one and return the resulting array of digits.

    def plusOne(self, digits: list[int]) -> list[int]:
        n = len(digits)
        for i in range(n - 1, -1, -1):
            digits[i] += 1
            digits[i] %= 10
            if digits[i] != 0:
                return digits
        return [1] + digits

    # You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n,
    # representing the number of elements in nums1 and nums2 respectively.
    # Merge nums1 and nums2 into a single array sorted in non-decreasing order.
    # The final sorted array should not be returned by the function, but instead be stored inside the array nums1.
    # To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged,
    # and the last n elements are set to 0 and should be ignored. nums2 has a length of n.



    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        k = m + n - 1
        i, j = m - 1, n - 1
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1


    # Given an integer array nums, return true if any value appears at least twice in the array,
    # and return false if every element is distinct.

    def containsDuplicate(self, nums: list[int]) -> bool:
        nums.sort()
        b = False
        i = 0
        while i < len(nums) + 1:
            if nums[i] == nums[i + 1]:
                b = True
                return b
            else:
                b = False
            i += 1
        return b


# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the nonzero elements.
# Note that you must do this in-place without making a copy of the array.

    def pushZerosToEnd(self,arr, n):
        count = 0  # Count of non-zero elements
        for i in range(n):
            if arr[i] != 0:
                # here count is incremented
                arr[count] = arr[i]
                count += 1
        while count < n:
            arr[count] = 0
            count += 1
        return arr



# You have a set of integers s, which originally contains all the numbers from 1 to n.
# Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set,
# which results in repetition of one number and loss of another number.
# You are given an integer array nums representing the data status of this set after the error.
# Find the number that occurs twice and the number that is missing and return them in the form of an array.


    def findErrorNums(self, nums):

        nums.sort()
        rep_miss = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):

                if nums[i] == nums[j]:
                    rep_miss.append(nums[i])

        for i in range(1, len(nums) + 1):
            if i not in nums:  # and abs(rep_miss[0]-i ==1) :
                rep_miss.append(i)

        return rep_miss

