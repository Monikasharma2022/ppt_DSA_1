class Solution(object):
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



    def isStrobogrammatic(self, num):

        maps = {("0", "0"), ("1", "1"), ("6", "9"), ("8", "8"), ("9", "6")}
        i, j = 0, len(num) - 1
        while i <= j:
            if (num[i], num[j]) not in maps:
                return False
            i += 1
            j -= 1
        return True



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



# ans 6
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


obj = Solution()
ans = obj.backspaceCompare('ab##ac','a#b#ac')
print(ans)