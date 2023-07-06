# 1. Write a Python program to reverse a string without using any built-in string reversal functions.
class Solution:
    def Rev_str(self, my_string : str):
        str=""
        for i in my_string:
            str=i+str
        print("Reversed string:",str)




#2. Implement a function to check if a given string is a palindrome.
    def isPalindrome(self, s):
        return s == s[::-1]



# 3. Write a program to find the largest element in a given list.
    def Largest_in_list(self, lst : list):
        lst.sort()            # sorting the list
        return lst[-1]        # printing the last element




# 4. Implement a function to count the occurrence of each element in a list.
    def Count_occ(self, lst :list):
        from collections import Counter
        print(Counter(lst))



# 5. Write a program to find the second largest element in a given list.
    def scnd_large(self, lst : list):
        lst.sort()            # sorting the list
        return lst[-2]        # printing the last element



# 6. Implement a function to remove duplicate elements from a list.
    def rem_duplicates(self, lst :list):
        # using list comprehension to remove duplicated from list
        res = []
        [res.append(x) for x in lst if x not in res]

        # printing list after removal
        print("The list after removing duplicates : "
              + str(res))



# 7. Write a program to calculate the factorial of a given number.
    def factorial(self,n):
        # single line to find factorial
        return 1 if (n == 1 or n == 0) else n * self.factorial(n - 1)



#8. Implement a function to check if a given number is prime.

    def chk_prime(self, num):
        # Check if the number is greater than 1

        if num > 1:
            for i in range(2, int(num / 2) + 1):
                if (num % i) == 0:
                    print(num, "is not a prime number")
                    break
            else:
                print(num, "is a prime number")
        # If the number is less than 1, its also not a prime number.
        else:
            print(num, "is not a prime number")




#9. Write a Python program to sort a list of integers in ascending order.

    def sort_list(self, lst: list):
        lst.sort()
        print(lst)



# 10. Implement a function to find the sum of all numbers in a list.
    def sum(numbers):
        total = 0
        for x in numbers:
            total += x
        return total




#11. Write a program to find the common elements between two lists.
    def common_elment(self, list1, list2):
        list1 = set(list1)
        list2 = set(list2)
        lst = list1.intersection(list2)
        return lst




#12. Implement a function to check if a given string is an anagram of another string.
    def isAnagram(self, a, b):
        if sorted(a) == sorted(b):
            return True
        else:
            return False



#13. Write a Python program to generate all permutations of a given string.
    def perm(self, iterabl):
        from itertools import permutations
        perms = [''.join(p) for p in permutations(iterabl)]
        return perms




#14. Implement a function to calculate the Fibonacci sequence up to a given number of terms.
    # def fibonacci(self,n):
    #     n1, n2 = 0, 1
    #     print(0)
    #     if n == 0 or n== 1:
    #         return
    #     for i in range(2, n+1):
    #         n3 = n1 + n2
    #         print(n3)
    #         n1 = n2
    #         n2 = n3

    def fibonacci(self,n):
        if (n <= 1):
            return n
        else:
            return (self.fibonacci(n - 1) + self.fibonacci(n - 2))




    # [1, 2, 3, 4, 5]
#15. Write a program to find the median of a list of numbers.
    def mediaN(self, lst:list):
        #sort list in ascending order
        lst.sort()

        #if length of list is even
        if len(lst) % 2 == 0:
            mid = int(len(lst)/2)
            n = lst[mid]+lst[mid-1]
            median = float(n)/2
            return median

        # if length of list is odd
        if len(lst) % 2 != 0:
            mid = len(lst)//2
            return lst[mid]




# 16. Implement a function to check if a given list is sorted in non-decreasing order.
    def non_dec(self, lst:list):

        # return false if sorted in decreasing order
        if (lst.sort(reverse=True)==lst):
            return False

        # return true if list is sorted in non decresing order
        else:
            return True



# 17. Write a Python program to find the intersection of two lists.
    def intersection_list(self, list1, list2):
        list3 = [value for value in list1 if value in list2]
        return list3



#18. Implement a function to find the maximum subarray sum in a given list.
    def maxSubArray(self, nums):   #kadane's algorithm
        max_sum = float('-inf')
        meh = 0
        for num in nums:
            meh = meh + num
            if meh > max_sum:
                max_sum = meh
            if meh < 0:
                meh = 0
        return max_sum



#19. Write a program to remove all vowels from a given string.
    def rem_vowel(self, string):
        vowels = ['a','e','i','o','u']
        result = [letter for letter in string if letter.lower() not in vowels]
        result = ''.join(result)
        print(result)




#20. Implement a function to reverse the order of words in a given sentence.
    def rev_words(self, s: str):
        words = s.split(' ')
        string = []
        for word in words:
            string.insert(0, word)

        print(" ".join(string))




#21. Write a Python program to check if two strings are anagrams of each other.
    def check(self,s1, s2):
        # the sorted strings are checked
        if (sorted(s1) == sorted(s2)):
            print("The strings are anagrams.")
        else:
            print("The strings aren't anagrams.")




#22. Implement a function to find the first non-repeating character in a string.
    def printNonrepeated(self, string):
        from collections import Counter
        # Calculating frequencies using Counter function
        freq = Counter(string)
        # Traverse the string
        for i in string:
            if (freq[i] == 1):
                print("First non-repeating character is " + i)
                break




#23. Write a program to find the prime factors of a given number.
    def primeFactors(self,n):
        import math
        # Print the number of two's that divide n
        while n % 2 == 0:
            print(2, end=" ")
            n = n / 2

        # n must be odd at this point so a skip of 2 ( i = i + 2) can be used
        for i in range(3, int(math.sqrt(n)) + 1, 2):

            # while i divides n , print i and divide n
            while n % i == 0:
                print(i, end= " ")
                n = n / i

        # Condition if n is a prime number greater than 2
        if n > 2:
            print(n)




#24. Implement a function to check if a given number is a power of two.
    def isPowerOfTwo(self,n):
        import math
        if n == 0:
            return False

        else:
            num = (math.log10(n) /
                math.log10(2))
        return (math.ceil(num) ==
                math.floor(num))



#25. Write a Python program to merge two sorted lists into a single sorted list.
    def merge_sort(self, lst1, lst2):
        # using sorted() to combine two sorted lists
        res = sorted(lst1 + lst2)

        # printing result
        print ("The combined sorted list is : ", res)




# 26. Implement a function to find the mode of a list of numbers.
    def get_mode(self, n_num):
        from collections import Counter
        data = Counter(n_num)
        get_mode = dict(data)
        mode = [k for k, v in get_mode.items() if v == max(list(data.values()))]

        if len(mode) == len(n_num):
            get_mode = "No mode found"
        else:
            get_mode = "Mode is / are: " + ', '.join(map(str, mode))

        print(get_mode)




#27. Write a program to find the greatest common divisor (GCD) of two numbers.
    def gcd(self, a, b):
        # Find minimum of a and b
        result = min(a, b)

        while result:
            if a % result == 0 and b % result == 0:
                break
            result -= 1
        return result    #return gcd of nmbrs



#28. Implement a function to calculate the square root of a given number.
    def countSquares(self, x):
        sqrt = x ** 0.5
        return sqrt



# 29. Write a Python program to check if a given string is a valid palindrome ignoring non-alphanumeric characters.
    def is_Palindrome(self,s):
        import re
        s  = re.sub(r'[\W_]', '', s)
        return s == s[::-1]




# 30. Implement a function to find the minimum element in a rotated sorted list.
    def findMin(self, arr):
        min_ele = arr[0]

        # Traversing over array to find minimum element
        for i in range(len(arr)):
            if arr[i] < min_ele:
                min_ele = arr[i]

        return min_ele




#31. Write a program to find the sum of all even numbers in a list.
    def sum_even(self, lst:list):
        sum = 0
        for i in range(len(lst)):
            if lst[i]%2 == 0:
                sum  += lst[i]
        return sum



#32. Implement a function to calculate the power of a number using recursion.
    def powr(self, num, raise_pow):
        if raise_pow == 0:
            return 1
        return num * self.powr(num, raise_pow-1)



#33. Write a Python program to remove duplicates from a list while preserving the order.
    def Remove(self, duplicate):
        final_list = []
        for num in duplicate:
            if num not in final_list:
                final_list.append(num)
        return final_list



#34. Implement a function to find the longest common prefix among a list of strings.
    def longestCommonPrefix(self, a:list):
        size = len(a)

        # if size is 0, return empty string
        if (size == 0):
            return ""

        if (size == 1):
            return a[0]

        # sort the array of strings
        a.sort()

        # find the minimum length from first and last string
        end = min(len(a[0]), len(a[size - 1]))

        # find the common prefix between the first and last string
        i = 0
        while (i < end and
               a[0][i] == a[size - 1][i]):
            i += 1

        prefix = a[0][0: i]
        return prefix




#35. Write a program to check if a given number is a perfect square.
    def isPerfectSquare(self, x):
        import math
        if(x >= 0):
            sr = int(math.sqrt(x))
            # sqrt function returns floating value so we have to convert it into integer return boolean T/F
            return ((sr*sr) == x)
        return False




#36. Implement a function to calculate the product of all elements in a list.
    def multiplyList(self, myList):

        # Multiply elements one by one
        result = 1
        for x in myList:
            result = result * x
        return result



#37. Write a Python program to reverse the order of words in a sentence while preserving the word order.
# repeated question 20



#38. Implement a function to find the missing number in a given list of consecutive numbers.
    def findMissing(self, arr, N):
        # create a list of zeroes
        temp = [0] * (N+1)

        for i in range(0, N):
            temp[arr[i] - 1] = 1

        for i in range(0, N+1):
            if(temp[i] == 0):
                ans = i + 1
                break

        print(ans)




#39. Write a program to find the sum of digits of a given number.
    def sumDigits(self, no):
        return 0 if no == 0 else int(no % 10) + self.sumDigits(int(no/10))




#40. Implement a function to check if a given string is a valid palindrome considering case sensitivity.
    def is__Palindrome(self,s):
        import re
        s  = re.sub(r'[\W_]', '', s)
        return s == s[::-1]




#41. Write a Python program to find the smallest missing positive integer in a list.
    def findSmallestMissing(self, nums):
        # initialize the set from array elements
        distinct = {*nums}

        # return first smallest missing positive number from the set
        index = 1
        while True:
            if index not in distinct:
                return index
            index += 1



#42. Implement a function to find the longest palindrome substring in a given string.
    def longestPalSubstr(self, str):

        # Get length of input String
        n = len(str)

        # All subStrings of length 1 are palindromes
        maxLength = 1
        start = 0

        # Nested loop to mark start and end index
        for i in range(n):
            for j in range(i, n):
                flag = 1

                # Check palindrome
                for k in range(0, ((j - i) // 2) + 1):
                    if (str[i + k] != str[j - k]):
                        flag = 0

                # Palindrome
                if (flag != 0 and (j - i + 1) > maxLength):
                    start = i
                    maxLength = j - i + 1


        print("Longest palindrome substring is: ", end="")

        for i in range(start, start + maxLength - 1):
            print(str[i], end="")
        print("")

        print("length is: ", end="")

        # Return length of LPS
        return maxLength




#43. Write a program to find the number of occurrences of a given element in a list.
    def count_occ(self, lst, x):
        from collections import Counter

        d = Counter(lst)
        print('{} has occurred {} times'.format(x, d[x]))




#44. Implement a function to check if a given number is a perfect number.
    def isPerfect(self, n):
        # To store sum of divisors
        sum = 1

        # Find all divisors and add them
        i = 2
        while i * i <= n:
            if n % i == 0:
                sum = sum + i + n / i
            i += 1

        # If sum of divisors is equal to n, then n is a perfect number

        return (True if sum == n and n != 1 else False)




# 45. Write a Python program to remove all duplicates from a string.
    def rem_duplicates(self, str):
        k2=[]
        for ele in str:
            if ele not in k2:
                k2.append(ele)
        for i in range(0,len(k2)):
            print(k2[i],end="")



# 46. Implement a function to find the first missing positive
    def first_missing(self, nums):
        nums.sort()  # sort the given array of numbers
        ans = 1  # set 1 as ans because 1 is the smallest positive integer#
        for i in range(len(nums)):
            if nums[
                i] == ans:  # if during the iteration current index value and ans matches then increment ans, at any point it does not match return ans #
                ans += 1
        return ans


obj = Solution()
# obj.Rev_str('Monika Gaur')
# ans = obj.isPalindrome("malayalam")
# ans = obj.Largest_in_list([10, 20, 4, 45, 99])
# obj.Count_occ([1,1,1,23,'m'])
# ans = obj.scnd_large([10, 20, 4, 45, 99])
# obj.rem_duplicates([11,1,1,2,2,5,56])
# ans = obj.factorial(5)
# obj.chk_prime(9)
# obj.sort_list([3,5,3,1,34,23,23,677,4])
# ans = obj.common_elment([11,1,1,2,2,5,56], [3,5,3,1,34,23,23,677,4])
# ans = obj.perm("abc")
# n = int(input("Enter the no of fibonacci terms:"))
# for i in range(n):
#     print(obj.fibonacci(i), end=" ")
# ans = obj.mediaN([1,4,2,5,0])
# ans = obj.non_dec([8,4,5,7,8,9])
# ans = obj.maxSubArray([-8,4,-5,7,8,-9])
# obj.rem_vowel("monika gaur")
# obj.rev_words("i love programming very much")
# obj.check('listen', 'silent')
# obj.printNonrepeated('geegs')
# obj.primeFactors(315)
# ans  = obj.isPowerOfTwo(24)
# obj.merge_sort([1, 5, 6, 9, 11],[3, 4, 7, 8, 10])
# obj.get_mode([2,3,5,7,8,6,4,3,2,2,3,4,5])
# ans = obj.gcd(30, 20)
# ans = obj.countSquares(26)
# ans = obj.is_Palindrome('1Mal$%^ayalam1')
# ans = obj.sum_even([1,2,3,4,5,6])
# ans = obj.powr(5, 3)
# ans = obj.longestCommonPrefix(["geeksforgeeks", "geek", "geeks", "geezer"])
# obj.findMissing([1,2,4,5,8,6, 7],7)
# ans = obj.findSmallestMissing([-1,1,2,3,1,4,5])
# ans = obj.longestPalSubstr("forgeeksskeegfor")
# ans = obj.count_occ([1, 1, 2, 2, 3, 3, 4, 4, 5, 5], 3)
# ans = obj.isPerfect(496)
# obj.rem_duplicates("fortherandomforest")
ans = obj.first_missing([-1,1,2,3,1,4,5])
print(ans)


