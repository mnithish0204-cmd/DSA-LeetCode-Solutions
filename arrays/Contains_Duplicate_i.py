from typing import List
"""
LeetCode 217 – Contains Duplicate

Category: Array
Approach: Hash Set

You are given an integer array nums.
Return True if any value appears at least twice in the array,
and return False if every element is distinct.

Idea:
Use a set to keep track of elements seen so far.
While iterating through the array:
- If the current number is already in the set, a duplicate exists.
- Otherwise, add the number to the set.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen=set()
        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)
        return False
