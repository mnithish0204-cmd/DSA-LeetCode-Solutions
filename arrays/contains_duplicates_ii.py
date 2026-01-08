from typing import List
# LeetCode 219 - Contains Duplicate II
# Category: Array, Hash Table
# Difficulty: Easy
#
# Approach:
# Use a hash map to store the last seen index of each number.
# Traverse the array using enumerate to get both index and value.
# If the current number already exists in the map, check the index difference.
# If the absolute difference between indices is less than or equal to k, return True.
# Update the index of the current number in the map.
# If no valid pair is found, return False.
#
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        last_seen={}
        for i,num in enumerate(nums):
            if num in last_seen and abs(i-last_seen[num]) <= k:
                return True
            else:
                last_seen[num]=i
        return False
        
