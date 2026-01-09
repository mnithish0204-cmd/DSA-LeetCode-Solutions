from typing import List 
# LeetCode 53 - Maximum Subarray
# Category: Array, Dynamic Programming
# Difficulty: Medium
#
# Approach:
# Use Kadane’s Algorithm to find the maximum sum of a contiguous subarray.
# Keep track of:
# 1. current_sum -> maximum subarray sum ending at the current index.
# 2. max_sum -> maximum subarray sum found so far.
# 
# At each element, decide whether to:
# - Start a new subarray from the current element, or
# - Continue the previous subarray by adding the current element.
# 
# Update max_sum at every step.
#
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum=nums[0]
        max_sum=nums[0]
        for num in nums[1:]:
            current_sum=max(num,current_sum+num)
            max_sum=max(max_sum,current_sum)
        return max_sum
        
