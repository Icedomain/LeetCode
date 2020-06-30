#
# @lc app=leetcode.cn id=59 lang=python3
#
# [59] 螺旋矩阵 II
#
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
    #def generateMatrix(self, n):
        '''
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
        '''

        mat = [[0] * n for _ in range(n)]
        i, j = 0, 0
        dx = [0,1,0,-1]
        dy = [1,0,-1,0]
        di = 0

        for k in range(n**2):
            mat[i][j] = k + 1
            # 非0 已填充
            if mat[(i+dx[di])%n][(j+dy[di])%n]:
                di = (di+1)%4
            i += dx[di]
            j += dy[di]
        return mat
