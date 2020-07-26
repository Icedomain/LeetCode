#
# @lc app=leetcode.cn id=174 lang=python3
#
# [174] 地下城游戏
#
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m,n = len(dungeon),len(dungeon[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]

        # 逆序遍历 逆序初始化
        # 需求值-所给值
        dp[m-1][n-1] = max(1-dungeon[m-1][n-1],1)
        for r in range(m-2,-1,-1):
            dp[r][n-1] = max(dp[r+1][n-1] -dungeon[r][n-1] ,1)
        for c in range(n-2,-1,-1):
            dp[m-1][c] = max(dp[m-1][c+1] -dungeon[m-1][c] ,1)
        # 从下往上从右往左遍历
        for r in range(m-2,-1,-1):
            for c in range(n-2,-1,-1):
                dp[r][c] = max(
                    min(dp[r][c+1] - dungeon[r][c] ,
                    dp[r+1][c]  - dungeon[r][c] ),
                    1)
        return dp[0][0]

