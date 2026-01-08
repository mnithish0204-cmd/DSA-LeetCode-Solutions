from typing import List 
# LeetCode 189 - Rotate Array
# Category: Array
# Difficulty: Medium
#
# Approach:
# Use the reversal algorithm to rotate the array in-place.
# First, reduce k using modulo to handle cases where k > array length.
# Reverse the entire array.
# Reverse the first k elements.
# Reverse the remaining n-k elements.
#
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        k=k%n

        nums.reverse()
        nums[:k] =reversed(nums[:k])
        nums[k:] = reversed(nums[k:])
