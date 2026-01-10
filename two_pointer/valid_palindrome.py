# LeetCode 125 - Valid Palindrome
# Category: String, Two Pointers
# Difficulty: Easy
#
# Approach:
# First, clean the given string by:
# 1. Keeping only alphanumeric characters (letters and digits).
# 2. Converting all characters to lowercase to ignore case sensitivity.
#
# After cleaning the string, check whether it is a palindrome by:
# - Comparing the cleaned string with its reversed version.
#
# If both strings are equal, the string is a valid palindrome.
#
# Time Complexity: O(n)
# Space Complexity: O(n)
#
# Where n is the length of the input string.
class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned=""
        for ch in s :
            if ch.isalnum():
                cleaned+=ch.lower()

        return cleaned==cleaned[::-1]

"""this code is the another method by using reversed() function """

class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned=""
        for ch in s :
            if ch.isalnum():
                cleaned+=ch.lower()

        return cleaned=="".join(reversed(cleaned))
