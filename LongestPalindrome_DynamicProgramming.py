
"""
Given a string s, return the longest palindromic substring in s.
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ''
        for i in range(len(s)):
            for j in range(i, len(s)):
                # checks for palindromes in string and sub-strings, updates to get the longest one
                if s[i]==s[j] and s[i:j+1] == s[i:j+1][::-1] and len(s[i:j+1]) > len(result):
                    result = s[i:j+1]
        return result

