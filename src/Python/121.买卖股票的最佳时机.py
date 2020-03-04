#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        minelement = float('inf')
        profit = 0
        for i in range(len(prices)):
            minelement = min(minelement, prices[i])
            profit = max(profit, prices[i] - minelement)
        return profit


