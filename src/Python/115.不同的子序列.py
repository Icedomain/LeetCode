#
# @lc app=leetcode.cn id=115 lang=python3
#
# [115] 不同的子序列
#
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if s is None or t is None :
            return 0
        ls = len(s)
        lt = len(t)
        dp = [ [0 for _ in range(lt+1) ] for _ in range(ls+1)]

        # init
        # 当母串子串都是0长度时，次数是1
        # 当子串长度为0时，所有次数都是1
        # 当母串长度为0时，所有次数都是0 (默认是0,不用重复了)
        for i in range(ls+1):
            dp[i][0] = 1
                
        for i in range(1,ls+1):
            for j in range(1,lt+1):
                dp[i][j] = dp[i-1][j]
                if s[i-1] == t[j-1]:
                    dp[i][j] += dp[i - 1][j - 1]
                
        return dp[-1][-1]
