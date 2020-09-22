#
# @lc app=leetcode.cn id=1314 lang=python3
#
# [1314] 矩阵区域和
#
class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        global m ,n 
        m, n = len(mat), len(mat[0])
        # 多一行 多一列
        P = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                P[i][j] = P[i - 1][j] + P[i][j - 1] \
                    + mat[i - 1][j - 1] - P[i - 1][j - 1] 

        res = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                l_x , l_y = max(i - K , 0) ,max(j - K , 0)
                r_x , r_y = min(i+K+1 ,m) , min(j+K+1 ,n)
                res[i][j] = P[r_x][r_y] - P[l_x][r_y] - \
                            P[r_x][l_y] + P[l_x][l_y]
        return res


