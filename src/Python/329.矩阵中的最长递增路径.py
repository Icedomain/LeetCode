#
# @lc app=leetcode.cn id=329 lang=python3
#
# [329] 矩阵中的最长递增路径
#
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        m, n = len(matrix), len(matrix[0])
        res = 0
        # 用于记录每个点的最长递增路径的长度
        cache = [[-1 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                # 每次寻找该点的最长递增路径的长度，并且更新全局的长度
                cur_len = self.dfs(matrix,i, j,  cache)
                res = max(res, cur_len)
        return res

    def dfs(self,matrix,i,j,cache):
        if cache[i][j] != -1:
            return cache[i][j]
        
        res = 0
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            x, y = i + dx, j + dy

            if x < 0 or y < 0 or x >= len(matrix) or\
                y >= len(matrix[0]) or matrix[x][y] <= matrix[i][j]:
                continue
            # x,y比i,j位置值大
            length = self.dfs(matrix,x, y,  cache)
            res = max(length, res)
        res += 1 # 加上当前的
        # 记录当前这个点的最长递增路径长度
        cache[i][j] = res
        return res
