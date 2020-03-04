#
# @lc app=leetcode.cn id=96 lang=python3
#
# [96] 不同的二叉搜索树
#
class Solution:
    def numTrees(self, n: int) -> int:
        f = [0 for _ in range(n+1)]
        f[0] = f[1] = 1
        for k in range(2,n+1):
            for i in range(k+1):
                f[k] += f[i-1]*f[k-i]
        return f[n]
