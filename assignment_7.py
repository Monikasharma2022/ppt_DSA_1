class Solution(object):

# ...............ans1......................

#Given two strings s and t, *determine if they are isomorphic*.
# Two strings s and t are isomorphic if the characters in s can be replaced to get t.
# All occurrences of a character must be replaced with another character while preserving the order of characters.
# No two characters may map to the same character, but a character may map to itself.

    def isisomorphic(str1, str2):
        if len(str1) != len(str2):
            return False
        else:
            map1, map2 = {}, {}
            for i in range(len(str1)):
                ch1, ch2 = str1[i], str2[i]
                if ch1 not in map1:
                    map1[ch1] = ch2
                if ch2 not in map2:
                    map2[ch2] = ch1
                if map1[ch1] != ch2 or map2[ch2] != ch1:
                    return False
        return True


 # ............ans2.....................
#Given a string num which represents an integer, return true *if* num *is a **strobogrammatic number***.
# A **strobogrammatic number** is a number that looks the same when rotated 180 degrees (looked at upside down).

    def isStrobogrammatic(self, num):

        maps = {("0", "0"), ("1", "1"), ("6", "9"), ("8", "8"), ("9", "6")}
        i, j = 0, len(num) - 1
        while i <= j:
            if (num[i], num[j]) not in maps:
                return False
            i += 1
            j -= 1
        return True


# ................ans3.......................
#Given two non-negative integers, num1 and num2 represented as string, return *the sum of* num1 *and* num2 *as a string*.
# You must solve the problem without using any built-in library for handling large integers (such as BigInteger).
# You must also not convert the inputs to integers directly.

    def addStrings(self, num1, num2):
        result = ""
        carry = 0

        def equalizeNumberOfCharacters(num1, num2):
            if len(num1) < len(num2):
                while len(num1) != len(num2):
                    num1 = "0" + num1
            else:
                while len(num2) != len(num1):
                    num2 = "0" + num2
            return [num1, num2]

        num1, num2 = equalizeNumberOfCharacters(num1, num2)

        num1Array = list(num1)
        num2Array = list(num2)

        while len(num1Array) != 0:
            add = int(num1Array.pop()) + int(num2Array.pop()) + int(carry)
            carry = add // 10
            result = str(add % 10) + result

        if carry != 0:
            result = str(carry) + result
        return result




# ...................ans4..........................
# Given a string s, reverse the order of characters in each word within a sentence
# while still preserving whitespace and initial word order.

    def reverseWords(self, string):
        st = list()
        # Traverse given string and push all characters to stack until we see a space.
        for i in range(len(string)):
            if string[i] != " ":
                st.append(string[i])
             # When we see a space, we print contents of stack.
            else:
                while len(st) > 0:
                    print(st[-1], end="")
                    st.pop()
                print(end=" ")
         # Since there may not be space after last word.
        while len(st) > 0:
            print(st[-1], end="")
            st.pop()



# .......................ans5............................
#Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start of the string.
# If there are fewer than k characters left, reverse all of them. If there are less than 2k but
# greater than or equal to k characters,then reverse the first k characters and leave the other as original.

    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        sLen = len(s)
        builder = ""
        left = 0
        rev = False
        for i in range(sLen):
            if i % k == 0:
                subStr = s[left:i]
                if rev:
                    subStr = subStr[::-1]
                builder += subStr
                left = i
                rev = not rev
        subStr = s[left:sLen]
        if rev:
            subStr = subStr[::-1]
        builder += subStr
        return builder



# ....................ans 6....................
# Given two strings s and goal, return true *if and only if* s *can become* goal *after some number of **shifts** on* s.
# A **shift** on s consists of moving the leftmost character of s to the rightmost position.

    def areRotations(self, string1, string2):
        size1 = len(string1)
        size2 = len(string2)
        temp = ''

        # Check if sizes of two strings are same
        if size1 != size2:
            return False

        # Create a temp string with value str1.str1
        temp = string1 + string1

        # Now check if str2 is a substring of temp
        # string.count returns the number of occurrences of
        # the second string in temp
        if (temp.count(string2) > 0):
            return True
        else:
            return False


# ..........................ans7...........................
# Given two strings s and t, return true *if they are equal when both are typed into empty text editors*.
# '#' means a backspace character.
# Note that after backspacing an empty text, the text will continue empty.

    def backspaceCompare(self, S: str, T: str) -> bool:
        def bckspc(string):
            stack=[]
            for i in string:
                if i =='#':
                    try:
                        stack.pop()
                    except:
                        pass
                else:
                    stack.append(i)
            return ''.join(stack)

        return (bckspc(S)==bckspc(T))



# ...........................ans8..........................
# Function to check if a straight line can be formed using N points
    def isStraightLinePossible(self, arr, n):
        # First pair of point (x0, y0)
        x0 = arr[0][0]
        y0 = arr[0][1]

        # Second pair of point (x1, y1)
        x1 = arr[1][0]
        y1 = arr[1][1]

        dx = x1 - x0
        dy = y1 - y0

        # Loop to iterate over the points
        for i in range(n):
            x = arr[i][0]
            y = arr[i][1]
            if (dx * (y - y1) != dy * (x - x1)):
                return False
        return True

arr = [[0, 0], [1, 1],
           [3, 3], [2, 2]]

obj = Solution()
ans = obj.isStraightLinePossible(arr, 4)
print(ans)


