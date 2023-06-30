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
    def fact(self, num):
        for i in range(1,num+1)
        print('The factorial of {} is {}'.num, factorial)



obj = Solution()
# obj.Rev_str('Monika Gaur')
# ans = obj.isPalindrome("malayalam")
# ans = obj.Largest_in_list([10, 20, 4, 45, 99])
# obj.Count_occ([1,1,1,23,'m'])
# ans = obj.scnd_large([10, 20, 4, 45, 99])
obj.rem_duplicates([11,1,1,2,2,5,56])
# print(ans)