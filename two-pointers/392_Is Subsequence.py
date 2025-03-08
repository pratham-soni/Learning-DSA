"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false

"""
str1 = "ahc"
str2 = "ahbgdc"

class Solution:
    def isSubsequence(self, str1: str, str2: str) -> bool:
        if len(str2) < len(str1):
            str1, str2 = str2, str1
        # Initialising indexes for both strings
        index1, index2 = 0,0
        # starting for loop to iterate over both strings at a same time
        while index1 < len(str1) and index2 < len(str2):
            if str1[index1] == str2[index2]:
                index1 +=1
                index2 +=1
            else:
                index2 +=1

        return True if index1 == len(str1) else False
    
sol = Solution()
print(sol.isSubsequence( str1, str2))