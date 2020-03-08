#
# @lc app=leetcode.cn id=63 lang=python3
#
# [63] 不同路径 II
#
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid:
            return 
        r, c = len(obstacleGrid), len(obstacleGrid[0])
        mat = [[0 for _ in range(c)] for _ in range(r)]
        # 到起点看这里有没有问题
        mat[0][0] = 1 - obstacleGrid[0][0]
        
        for i in range(1, r):
            mat[i][0] = mat[i-1][0] * (1 - obstacleGrid[i][0])
        for i in range(1, c):
            mat[0][i] = mat[0][i-1] * (1 - obstacleGrid[0][i])
        
        for i in range(1, r):
            for j in range(1, c):
                mat[i][j] = (mat[i][j-1] + mat[i-1][j]) * (1 - obstacleGrid[i][j])
        return mat[-1][-1]


