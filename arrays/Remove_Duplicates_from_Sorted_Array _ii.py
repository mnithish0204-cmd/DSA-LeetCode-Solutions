from typing import List
# LeetCode 26 - Remove Duplicates from Sorted Array
# Category: Array, Two Pointers
# Difficulty: Easy
#
# Approach:
# Since the array is sorted, duplicate elements appear consecutively.
# Use two pointers:
# - One pointer iterates through the array.
# - Another pointer tracks the position for the next unique element.
# When a new value is found, overwrite the element at the unique index.
# The array is modified in-place without using extra space.
#
# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k=2
        for i in range(2,len(nums)):
            if nums[i]!=nums[k-2]:
                nums[k]=nums[i]
                k+=1
        return k
