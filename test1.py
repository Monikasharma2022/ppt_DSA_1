# Given a string s, find the first non-repeating character in it and return its index.
# If it does not exist, return -1.

class Solution(object):
    def firstUniqChar(self, string):
        index = 0
        if len(string) == 0:
            print("empty string!!!")

        for i in string:
            if string.count(i) == 1:
                return string.index(i)
            else:
                index += 1
        if index == len(string) :
            return -1


