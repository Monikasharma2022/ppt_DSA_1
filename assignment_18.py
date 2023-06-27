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




obj = Solution()
# ans = obj.merge([[1,3],[2,6],[8,10],[15,18]])
# ans = obj.sortColors([0,2,1,1,0,0,2,1])
ans = obj.maximumGap([3,6,9,1])
print(ans)