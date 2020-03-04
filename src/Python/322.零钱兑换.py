#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
#

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        if coins is None or len(coins) == 0:
            return -1
        
        coins.sort()
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for j in range(coin, amount+1):
                dp[j] = min(dp[j], dp[j - coin] + 1)

        return -1 if dp[-1] > amount else dp[-1]

