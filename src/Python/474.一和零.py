#
# @lc app=leetcode.cn id=474 lang=python3
#
# [474] 一和零
#
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        if not strs:
            return 0
        # 准备很多个背包
        dp = [ [0]*(n+1) for _ in range(m+1)]
        
        for str in strs:
            count0 = str.count('0')
            count1 = str.count('1')
            
            # 遍历可容纳的背包 
            for zeroes in range(m, count0 - 1, -1):
                for ones in range(n, count1 - 1, -1):
                    dp[zeroes][ones] = max(dp[zeroes][ones] ,
                    1 + dp[zeroes - count0][ones - count1])
        return dp[m][n] 

