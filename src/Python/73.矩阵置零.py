#
# @lc app=leetcode.cn id=73 lang=python3
#
# [73] 矩阵置零
#
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        '''
        # 直接法
        row = []
        col = []
        hang = len(matrix)
        lie = len(matrix[0])
        for i in range(hang):
            for j in range(lie):
                if matrix[i][j] == 0:
                    row.append(i)
                    col.append(j)
        row = set(row)
        col = set(col)

        for i in row:
            for j in range(lie):
                matrix[i][j] = 0
        for j in col :
            for i in range(hang):
                matrix[i][j] =0
        
        return matrix
        '''
        firstRowHasZero = not all(matrix[0])
        hang = len(matrix)
        lie = len(matrix[0])
        # 第一行第一列做标记
        for i in range(1,hang):
            for j in range(lie):
                if matrix[i][j] == 0:
                    matrix[0][j] = matrix[i][0] = 0
        # 置0
        for i in range(1,hang):
            for j in range(lie-1,-1,-1):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        # 补一下第一行的
        
        if firstRowHasZero:
            matrix[0] = [0] * lie
        
        return matrix




        


        

