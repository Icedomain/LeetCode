#
# @lc app=leetcode.cn id=1139 lang=python3
#
# [1139] 最大的以 1 为边界的正方形
#
class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        # l表示点i,j左侧连续0的个数        |
        # u表示i,j上方连续0的个数   _______|
        left = [[0 for _ in range(n)] for _ in range(m)]
        up = [[0 for _ in range(n)] for _ in range(m)]

        maxLen = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    left[i][j], up[i][j] = 1, 1
                    if i> 0:
                        up[i][j] += up[i-1][j]
                    if j > 0:
                        left[i][j] += left[i][j-1]
                    # 边长遍历
                    for k in range(min(up[i][j], left[i][j]), 0, -1):
                        # 左边上方 上方左边
                        if k > maxLen and \
                        up[i][j-k+1] >= k and \
                        left[i-k+1][j] >= k:
                            maxLen = k
                            break
        return maxLen**2

