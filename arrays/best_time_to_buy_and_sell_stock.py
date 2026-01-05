from typing import List

"""
LeetCode 121 – Best Time to Buy and Sell Stock

Category: Array
Approach: Greedy (One Pass)

You are given an array prices where prices[i] is the price of a stock on day i.
Choose one day to buy and a later day to sell to maximize profit.

If no profit is possible, return 0.

Example:
Input: prices = [7,1,5,3,6,4]
Output: 5

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = float('inf')

        for price in prices:
            if price < min_price:
                min_price = price
            else:
                current_profit = price - min_price
                max_profit = max(max_profit, current_profit)

        return max_profit

