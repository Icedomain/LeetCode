#
# @lc app=leetcode.cn id=695 lang=python3
#
# [695] 岛屿的最大面积
#
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    temp = self.dfs(grid, i, j)
                    res = max(res,temp)
        return res

    def dfs(self, grid, i, j):
        # 终止条件
        if i <  0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == 0:
            return 0

        # 四个方向搜索
        grid[i][j] = 0
        res = 1
        res += self.dfs(grid, i-1, j)
        res += self.dfs(grid, i, j-1)
        res += self.dfs(grid, i+1, j)
        res += self.dfs(grid, i, j+1)

        return res

