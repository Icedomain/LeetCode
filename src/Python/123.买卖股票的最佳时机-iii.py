#
# @lc app=leetcode.cn id=123 lang=python3
#
# [123] 买卖股票的最佳时机 III
#
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        """
        对于任意一天考虑四个变量:
        fstBuy: 在该天第一次买入股票可获得的最大收益 
        fstSell: 在该天第一次卖出股票可获得的最大收益
        secBuy: 在该天第二次买入股票可获得的最大收益
        secSell: 在该天第二次卖出股票可获得的最大收益
        分别对四个变量进行相应的更新, 最后secSell就是最大
        收益值(secSell >= fstSell)
        """
        fstBuy,fstSell= -float('inf'),0
        secBuy,secSell= -float('inf'),0
        for i in prices:
            fstBuy = max(fstBuy, -i)
            fstSell = max(fstSell, fstBuy + i)
            secBuy = max(secBuy, fstSell - i)
            secSell = max(secSell, secBuy + i)
        return secSell
        '''
        if not prices:
            return 0
        num = len(prices)

        forward  = [0]*num
        backward = [0]*num
        # 前向
        current_min = prices[0] 
        for i in range(1,len(prices)):
            current_min = min(current_min, prices[i])
            forward[i] = max(forward[i-1] , prices[i]-current_min )
        # 后向
        total_max = 0
        current_max = prices[-1]
        for i in range(len(prices) - 2, -1, -1):
            current_max = max(current_max, prices[i])
            backward[i] = max(backward[i+1], current_max - prices[i])
            total_max = max(total_max, backward[i] + forward[i])
        return total_max

