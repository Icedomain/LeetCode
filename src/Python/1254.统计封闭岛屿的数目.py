#
# @lc app=leetcode.cn id=1254 lang=python3
#
# [1254] 统计封闭岛屿的数目
#

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        cnt = 0
        for i in range(1, len(grid)-1):
            for j in range(1, len(grid[0])-1):
                if grid[i][j] == 0 and self.dfs(grid, i , j):
                    cnt += 1
        return cnt
    
    def dfs(self, grid, i, j):
        if grid[i][j] == 1:
            return True
        if i <= 0 or j <= 0 or i >= len(grid)-1 or j >= len(grid[0])-1:
            return False

        grid[i][j] = 1
        up = self.dfs(grid, i+1, j)
        down = self.dfs(grid, i-1, j)
        left = self.dfs(grid, i, j-1)
        right = self.dfs(grid, i, j+1)
        return up and down and left and right

