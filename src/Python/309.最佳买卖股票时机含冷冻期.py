#
# @lc app=leetcode.cn id=309 lang=python3
#
# [309] 最佳买卖股票时机含冷冻期
#
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        sale = [0 for _ in range(len(prices))]
        buy = [0 for _ in range(len(prices))]
        cool = [0 for _ in range(len(prices))]
        
        buy[0] = -prices[0]
        
        for i in range(1, len(prices)):
            cool[i] = sale[i-1]
            buy[i] = max(buy[i-1], cool[i-1] - prices[i])
            sale[i] = max(sale[i-1], buy[i] + prices[i])
        
        return max(sale[-1], cool[-1])   


