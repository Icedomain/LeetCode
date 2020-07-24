#
# @lc app=leetcode.cn id=221 lang=python3
#
# [221] 最大正方形
#
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix: 
            return 0
        row ,col = len(matrix) ,len(matrix[0])

        # 多了一行一列
        dp = [ [0 for _ in range(col + 1)] for _ in range(row + 1)]
        res = 0
        for i in range(1, row +1):
            for j in range(1, col + 1):
                if matrix[i - 1][j - 1] == "1":
                    # 否则dp为0, 不用操作
                    dp[i][j] = min(dp[i-1][j - 1],
                                   dp[i - 1][j],
                                   dp[i][j - 1]
                                   ) + 1
                    res = max(res, dp[i][j] ** 2)
        return res

