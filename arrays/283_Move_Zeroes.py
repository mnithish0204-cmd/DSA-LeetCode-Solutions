from typing import List
# LeetCode 283 - Move Zeroes
# Category: Array, Two Pointers
# Difficulty: Easy
#
# Approach:
# Use a two-pointer technique.
# One pointer scans the array, and the other tracks the position
# where the next non-zero element should be placed.
# Each time a non-zero is found, it is swapped to the front.
#
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        pos = 0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[pos] , nums[i] = nums[i] , nums[pos]
                pos += 1
