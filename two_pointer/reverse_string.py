# LeetCode 344 - Reverse String
# Category: Two Pointers, Array
# Difficulty: Easy
#
# Approach:
# Use the two-pointer technique to reverse the character array in-place.
# Initialize one pointer at the start (left) and another at the end (right).
# Swap the characters at these pointers and move them toward the center
# until they meet.
#
# This approach modifies the input list directly without using extra memory.
#
# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left,right = 0,len(s)-1
        while left<right:
            s[left],s[right] = s[right],s[left]
            left += 1
            right -= 1
