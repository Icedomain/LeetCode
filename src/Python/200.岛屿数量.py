#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        m,n = len(grid),len(grid[0])

        res = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1":
                    res += 1
                    self.dfs(grid,r,c,m,n)
        return res

    def dfs(self,grid,i,j,row,col):
        # 终止条件
        if i < 0 or j < 0 or i >= row or j >= col or grid[i][j] == "0":
            return 
        # 合法的话置位
        grid[i][j] = "0"
        self.dfs(grid,i-1,j,row,col)
        self.dfs(grid,i,j-1,row,col)
        self.dfs(grid,i+1,j,row,col)
        self.dfs(grid,i,j+1,row,col)


