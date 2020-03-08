#
# @lc app=leetcode.cn id=174 lang=python3
#
# [174] 地下城游戏
#
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m,n = len(dungeon),len(dungeon[0])
        res = [[0 for _ in range(n)] for _ in range(m)]

        # 逆序遍历
        # 逆序初始化
        res[m-1][n-1] = max(-dungeon[m-1][n-1],0)+1
        for r in range(m-2,-1,-1):
            res[r][n-1] = max(res[r+1][n-1] -dungeon[r][n-1] ,1)
        for c in range(n-2,-1,-1):
            res[m-1][c] = max(res[m-1][c+1] -dungeon[m-1][c] ,1)
        # 从下往上从右往左遍历
        for r in range(m-2,-1,-1):
            for c in range(n-2,-1,-1):
                res[r][c] = max(
                    min(res[r][c+1],res[r+1][c]) - dungeon[r][c],
                    1)
        return res[0][0]

