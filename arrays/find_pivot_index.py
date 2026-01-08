from typing import List 
# LeetCode 724 - Find Pivot Index
# Category: Array, Prefix Sum
# Difficulty: Easy
#
# Approach:
# First, calculate the total sum of the array.
# Initialize left_sum as 0.
# Traverse the array index by index.
# For each index i:
#   - Right sum is calculated as (total_sum - left_sum - nums[i]).
#   - If left_sum equals right sum, return the current index as pivot.
# Update left_sum by adding nums[i] after each iteration.
# If no pivot index is found, return -1.
#
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum=sum(nums)
        left_sum=0
        for i in range(len(nums)):
            if left_sum==total_sum - left_sum - nums[i]:
                return i
            left_sum+= nums[i]
        return -1
