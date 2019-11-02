"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one
 and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if len(prices) < 2:
            return 0

        i = prices[0]
        diff = 0
        i1 = 1
        profit = 0
        while i1 < len(prices):
            if i < prices[i1]:
                if i1 == len(prices) - 1:
                    if diff <= (prices[i1] - i):
                        diff = prices[i1] - i
                        i1 = i1 + 1
                    profit = profit + diff
                    break
                else:
                    if diff <= (prices[i1] - i):
                        diff = prices[i1] - i
                        i1 = i1 + 1
                    else:
                        profit = profit + diff
                        diff = 0
                        i = prices[i1]
                        i1 = i1 + 1
            else:
                i = prices[i1]
                profit = profit + diff
                diff = 0
                i1 = i1 + 1

        return profit



