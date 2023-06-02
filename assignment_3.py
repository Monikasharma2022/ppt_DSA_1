# ..............ans 1................

# class Solution:
#     def closest_sum(self, nums, target):
#         nums.sort()
#         res = nums[0] + nums[1] + nums[2]
#
#         for i in range(len(nums) - 2):
#             l, r = i + 1, len(nums) - 1
#             while l < r:
#                 s = nums[i] + nums[l] + nums[r]
#                 if s == target:
#                     return s
#                 if abs(s - target) < abs(res - target):
#                     res = s
#                 if s < target:
#                     l += 1
#                 else:
#                     r -= 1
#
#         return res

# Time Complexity: O(n²)
#
# Space Complexity: O(1) or O(n)



# ..............ans 2................

# Store the pair of indices
class Pair():
    def __init__(self, x, y):
        self.index1 = x
        self.index2 = y

# Function to find the all the unique quadruplets
# with the elements at different indices
def GetQuadruplets(nums, target):
# Store the sum mapped to a list of pair indices
    map = {}

# Generate all possible pairs for the map
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            # Find the sum of pairs of elements
            sum = nums[i] + nums[j]

            # If the sum doesn't exist then update with the new pairs
            if sum not in map:
                map[sum] = [Pair(i, j)]
            # Otherwise, add the new pair of indices to the current sum
            else:
                map[sum].append(Pair(i, j))

    # Store all the Quadruplets
    ans = set()
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            lookUp = target - (nums[i] + nums[j])
            # If the sum with value (K - sum) exists
            if lookUp in map:
                # Get the pair of indices of sum
                temp = map[lookUp]
                for pair in temp:
                    # Check if i, j, k and l are distinct or not
                    if pair.index1 != i and pair.index1 != j and pair.index2 != i and pair.index2 != j:
                        l1 = [nums[pair.index1], nums[pair.index2], nums[i], nums[j]]
                        # Sort the list to avoid duplicacy
                        l1.sort()
                        # Update the set
                        ans.add(tuple(l1))
    # Print all the Quadruplets
    print(*reversed(list(ans)), sep = '\n')

# Driver Code
arr = [1, 0, -1, 0, -2, 2]
K = 0

GetQuadruplets(arr, K)



# ..............ans 3................


def reverse(nums, i, j):
    while i < j:
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
        j -= 1
def nextPermutation(nums: list[int]):
    # Length of the array
    n = len(nums)
    # Index of the first element that is smaller than
    # the element to its right.
    index = -1
    # Loop from right to left
    for i in range(n - 1, 0, -1):
        if nums[i] > nums[i - 1]:
            index = i - 1
            break
    # Base condition
    if index == -1:
        reverse(nums, 0, n - 1)
        return
    j = n - 1
    # Again swap from right to left to find first element
    # that is greater than the above find element
    for i in range(n - 1, index, -1):
        if nums[i] > nums[index]:
            j = i
            break
    # Swap the elements
    nums[index], nums[j] = nums[j], nums[index]
    # Reverse the elements from index + 1 to the nums.length
    reverse(nums, index + 1, n - 1)

# TC = O(n)
# SC = O(1)



# ..............ans 4................


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # Last and First indexes
        start = 0
        end = len(nums) - 1

        # Traverse an array
        while (start <= end):

            mid = (start + end) / 2

            # if target value found.
            if nums[mid] == target:
                return mid

            # If target value is greater then mid elements's value
            elif target > nums[mid]:
                start = mid + 1

            # otherwise target value is less,
            else:
                end = mid - 1
        # Return the insertion position
        return end + 1




# ..............ans 5................


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digit_length = len(digits)

        i = digit_length - 1

        while digits[i] == 9 and i >= 0:
            i -= 1

        if i == -1:
            results = [0] * (digit_length + 1)
            results[0] = 1
            return results

        results = [0] * (digit_length)

        results[i] = digits[i] + 1

        for j in range(i - 1, -1, -1):
            results[j] = digits[j]

        return results

# TC = O(n)
# SC = O(n+1)



# ..............ans 6................


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hash_table = {}
        for i in nums:
            try:
                hash_table.pop(i)
            except:
                hash_table[i] = 1
        return hash_table.popitem()[0]



# ..............ans 7................


# Print all elements of range
# [low, high] that are not
# present in arr[0..n-1]
def printMissing(arr, n, low, high):
    # Insert all elements of
    # arr[] in set
    s = set(arr)

    # Traverse through the range
    # and print all missing elements
    for x in range(low, high + 1):
        if x not in s:
            print(x, end=' ')


# Driver Code
arr = [1, 3, 5, 4]
n = len(arr)
low, high = 1, 10
printMissing(arr, n, low, high)



# ..............ans 8................


def canAttendMeetings(intervals):
    intervals.sort(key=lambda a: a.start)
    for i in range(len(intervals) - 1):
        if intervals[i].end > intervals[i + 1].start:
            return False
    return True