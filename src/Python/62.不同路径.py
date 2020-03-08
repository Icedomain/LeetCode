#
# @lc app=leetcode.cn id=62 lang=python3
#
# [62] 不同路径
#
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        mat = [[0 for _ in range(n)] for _ in range(m)] 
        for r in range(m):
            mat[r][0] = 1
        for c in range(n):
            mat[0][c] = 1
        for r in range(1,m):
            for c in range(1,n):
                mat[r][c] = mat[r-1][c] + mat[r][c-1]
        return mat[-1][-1]

