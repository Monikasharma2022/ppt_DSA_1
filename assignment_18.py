# ............................................ans 1................................................................

class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda x: x[0])
        merged = []
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged





# ...................................................ans 2.........................................
    def sortColors(self, nums: list[int]):
        zero=nums.count(0)
        one=nums.count(1)
        two=nums.count(2)
        for x in range(len(nums)):
            if two:
                nums.pop()
                nums.insert(0,2)
                two-=1
            elif one:
                nums.pop()
                nums.insert(0,1)
                one-=1
            else:
                nums.pop()
                nums.insert(0,0)
        return nums




# ............................................ans 3..............................................
    # where API isBadVersion is alreaady defined
    def firstBadVersion(self, n):
        first = 0
        last = n
        while first <= last:
            mid = (first + last) // 2
            if isBadVersion(mid):
                if not isBadVersion(mid - 1):
                    return mid
                else:
                    last = mid - 1
            else:
                first = mid + 1

        return -1




# .................................................ans4........................................
    def maximumGap(self, nums):
        if len(nums) < 2:
            return 0

        nums.sort()
        max_gap = 0

        for i in range(1, len(nums)):
            max_gap = max(max_gap, nums[i] - nums[i - 1])

        return max_gap




# ......................................................ans 5....................................................
    def containsDuplicate(self, nums: list[int]) -> bool:
        # Create an empty hash set
        seen = set()
        # Iterate over the array
        for num in nums:
            # If an element is already in the hash set, return True
            if num in seen:
                return True
            # Otherwise, add the element to the hash set
            seen.add(num)
        # If we finish iterating over the array and have not found a duplicate, return False
        return False




# ...........................................................ans 6...............................................
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        # Sort the balloons by their end points in ascending order
        points.sort(key=lambda x: x[1])

        # Initialize the number of arrows needed and the end point of the last arrow
        arrows = 0
        last_end = float('-inf')

        # Iterate through the balloons
        for start, end in points:
            # If the current balloon starts after the end of the last arrow, shoot a new arrow
            if start > last_end:
                arrows += 1
                last_end = end

        return arrows





# ...................................................................ans 7........................................................
    def lengthOfLIS(self, nums: list[int]) -> int:
        n = len(nums)
        tails = [0] * n # initialize tails array with 0
        size = 0
        for num in nums:
            i, j = 0, size
            while i != j:
                m = (i + j) // 2
                if tails[m] < num:
                    i = m + 1
                else:
                    j = m
            tails[i] = num
            size = max(i + 1, size)

        return size




# .........................................................ans 8.......................................................
    def find132pattern(self, nums: list[int]) -> bool:
        stack = []
        s3 = float('-inf')

        for i in range(len(nums) - 1, -1, -1):
            if nums[i] < s3:
                return True
            while stack and stack[-1] < nums[i]:
                s3 = stack.pop()
            stack.append(nums[i])

        return False



obj = Solution()
# ans = obj.merge([[1,3],[2,6],[8,10],[15,18]])
# ans = obj.sortColors([0,2,1,1,0,0,2,1])
# ans = obj.maximumGap([3,6,9,1])
# ans = obj.lengthOfLIS([10,9,2,5,3,7,101,18])
ans = obj.find132pattern([-1,3,2,0])
print(ans)