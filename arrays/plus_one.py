from typing import List
# LeetCode 66 - Plus One
# Category: Array, Math
# Difficulty: Easy
#
# Approach:
# Start from the last digit and simulate manual addition.
# If the current digit is less than 9, increment it and return the array.
# If the digit is 9, set it to 0 and continue to propagate the carry.
# If all digits are 9, add a new leading 1 to the array.
#
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1,-1,-1):
            if digits[i]<9:
                digits[i]+=1
                return digits
            digits[i]=0
        return [1]+digits
