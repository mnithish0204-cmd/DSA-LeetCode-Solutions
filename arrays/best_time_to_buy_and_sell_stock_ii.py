from typing import List
"""
LeetCode 122 – Best Time to Buy and Sell Stock II

Category: Array
Approach: Greedy

You are given an array prices where prices[i] is the price of a stock on day i.
You may complete as many transactions as you like (buy one and sell one share
of the stock multiple times).

Note:
- You must sell the stock before buying again.
- You can only hold one stock at a time.

Idea:
Whenever there is a profit opportunity (prices[i] > prices[i-1]),
take it by adding the difference to the total profit.

This works because all increasing segments together give the maximum profit.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
      profit=0
      for i in range(1,len(prices)):
        if prices[i]>prices[i-1]:
          profit += prices[i] -prices[i-1]
      return profit
