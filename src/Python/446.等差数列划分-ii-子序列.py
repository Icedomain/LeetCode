#
# @lc app=leetcode.cn id=446 lang=python3
#
# [446] 等差数列划分 II - 子序列
#

class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        if len(A) < 3:
            return 0
        res = 0
        dp = [{} for _ in range(len(A))]

        for i in range(1, len(A)):
            for j in range(i):
                diff = A[i] - A[j]
                # 这里的加1表示考虑(j, i)这样子的数列，
                # 因为只要出现能和(j, i)组成等差数列的值k，对于k来说这个1的必须的 
                if diff in dp[j]:
                    dp[i][diff] = dp[j][diff] + dp[i].get(diff, 0) + 1
                    res += dp[j][diff]
                else:
                    dp[i][diff] = dp[i].get(diff, 0) + 1
        return res
