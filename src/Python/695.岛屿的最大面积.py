#
# @lc app=leetcode.cn id=695 lang=python3
#
# [695] 岛屿的最大面积
#
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    ans = max(self.dfs(grid, i, j), ans)
                    # ans = max(self.bfs(grid, i, j), ans)
        return ans

    def dfs(self, grid, i, j):
        # DFS based on stack
        stack = [(i, j)]
        area = 0
        # Stack for DFS
        while stack:
            r, c = stack.pop(-1)
            area += 1
            for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if (0 <= nr < len(grid) and
                        0 <= nc < len(grid[0]) and grid[nr][nc]):
                    stack.append((nr, nc))
                    grid[nr][nc] = 0
        return area        

