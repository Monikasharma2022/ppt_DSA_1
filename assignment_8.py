class Solution(object):

# Given two strings s1 and s2, return the lowest ASCII sum of deleted characters to make two strings equal.

    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        dp = [[0] * (len(s2)+1) for _ in range(2)]
        for j in range(len(s2)):
            dp[0][j+1] = dp[0][j] + ord(s2[j])

        for i in range(len(s1)):
            dp[(i+1)%2][0] = dp[i%2][0] + ord(s1[i])
            for j in range(len(s2)):
                if s1[i] == s2[j]:
                    dp[(i+1)%2][j+1] = dp[i%2][j]
                else:
                    dp[(i+1)%2][j+1] = min(dp[i%2][j+1] + ord(s1[i]), \
                                           dp[(i+1)%2][j] + ord(s2[j]))

        return dp[len(s1)%2][-1]


# ..............ans 2....................
    def checkValidString(self, s: str) -> bool:
        open_count, close_count = 0, 0
        length = len(s) - 1
        for i in range(length + 1):
            if s[i] == '(' or s[i] == '*':
                open_count += 1
            else:
                open_count -= 1
            if s[length - i] == ')' or s[length - i] == '*':
                close_count += 1
            else:
                close_count -= 1
            if open_count < 0 or close_count < 0:
                return False
        return True


# ......................ans 3......................
    def minDistance(self, W1: str, W2: str) -> int:
        m, n = len(W1), len(W2)
        if m < n: W1, W2, m, n = W2, W1, n, m
        dpLast, dpCurr = [0] * (n + 1), [0] * (n + 1)
        for c1 in W1:
            for j in range(n):
                dpCurr[j + 1] = dpLast[j] + 1 if c1 == W2[j] else max(dpCurr[j], dpLast[j + 1])
            dpLast, dpCurr = dpCurr, dpLast
        return m + n - 2 * dpLast[n]


obj = Solution()
ans = obj.minimumDeleteSum('sea','eat')
print(ans)