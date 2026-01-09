from typing import List
# LeetCode 242 - Valid Anagram
# Category: String, Hash Table
# Difficulty: Easy
#
# Approach:
# Use Python's Counter to count the frequency of each character in both strings.
# Compare the two Counter objects.
# If the character frequencies are equal, the strings are anagrams.
# Otherwise, they are not anagrams.
#
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if Counter(s)==Counter(t):
            return True
        else:
            return False
