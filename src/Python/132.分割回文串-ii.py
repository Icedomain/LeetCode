#
# @lc app=leetcode.cn id=132 lang=python3
#
# [132] 分割回文串 II
#
class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]
        # f[0->n](共n+1个)  f[n-1]=0 , f[n]=-1
        # f(i) [i, n-1]最小裁剪数
        f = [n] *(n+1)
        f[n-1] = 0
        f[n] = -1
        # f 从右往左更新
        # dp (i 往左更新,j往右更新)
        for i in range(n-1,-1,-1):
            for j in range(i,n):
                if (s[i] == s[j] and (j - i < 2 or dp[i + 1][j - 1])) :
                    dp[i][j] = True
                    # 如果满足回文的条件
                    # f 选取裁剪更少的方案
                    f[i] = min(f[i], f[j + 1] + 1)
        return f[0]

