#
# @lc app=leetcode.cn id=59 lang=python3
#
# [59] 螺旋矩阵 II
#
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        mat = [[0 for _ in range(n)] for _ in range(n)]

        b,e = 0 , n - 1
        val = 1
        while b < e :
            # 横
            for i in range(b,e):
                mat[b][i] = val
                val += 1
            # 竖
            for i in range(b,e):
                mat[i][e] = val
                val += 1                
            # 横
            for i in range(e,b,-1):
                mat[e][i] = val
                val += 1
            # 竖
            for i in range(e,b,-1):
                mat[i][b] = val
                val += 1 
            b += 1
            e -= 1

        # n为奇数,中间还有一个值
        if n % 2 :
            mat[b][e] = val
        return mat
