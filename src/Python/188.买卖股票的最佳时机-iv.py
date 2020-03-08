#
# @lc app=leetcode.cn id=188 lang=python3
#
# [188] 买卖股票的最佳时机IV
#
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        #交易次数太多，用贪心
        if k >= len(prices)//2:
            return self.greedy(prices)
        
        # k=0的时候此时sell为空
        # k小，动态规划
        buy, sell = [-prices[0]]*k , [0]*(k+1)
        for p in prices[1:]:
            for i in range(k):
                # 买的收益 = max(买、买了再买)
                buy[i] = max(buy[i], sell[i-1]-p)
                # 卖的收益 = (卖/买)
                sell[i] = max(sell[i], buy[i]+p)
                
        return max(sell)
        
    def greedy(self, prices):
        res = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                res += prices[i] - prices[i-1]
        return res


