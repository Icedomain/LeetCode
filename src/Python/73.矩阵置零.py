#
# @lc app=leetcode.cn id=73 lang=python3
#
# [73] 矩阵置零
#
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        '''
        # 直接法
        row = []
        col = []
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row.append(i)
                    col.append(j)
        row = set(row)
        col = set(col)

        for i in row:
            for j in range(n):
                matrix[i][j] = 0
        for j in col :
            for i in range(m):
                matrix[i][j] =0
        
        return matrix
        '''
        # 第一行出现一个0
        firstRowHasZero = not all(matrix[0])
        is_col = False if matrix[0][0] else True
        m = len(matrix)
        n = len(matrix[0])
        # 第一行第一列做标记
        for i in range(1,m):
            if matrix[i][0] == 0:
                is_col = True
            for j in range(1,n):
                if matrix[i][j] == 0:
                    matrix[0][j] = matrix[i][0] = 0
        # 置0
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        # 补一下第一行 第一列        
        if firstRowHasZero:
            matrix[0] = [0] * n
        if is_col:
            for i in range(m):
                matrix[i][0] = 0
        return
