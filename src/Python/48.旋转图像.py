#
# @lc app=leetcode.cn id=48 lang=python3
#
# [48] 旋转图像
#
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        if matrix is None or len(matrix) == 1:
            return
        '''
        ls = len(matrix)

        for i in range(ls // 2):
            # 那一圈的半行
            begin, end = i, ls - 1 - i # 左右都往内部i个单位
            for k in range(ls- 1 - 2 * i ): # 减两个i的单位
                # 顺着转
                temp = matrix[end - k][begin] # 左下角
                matrix[end - k][begin] = matrix[end][end - k] # 右下角给左下角
                matrix[end][end - k] = matrix[begin + k][end] # 右上角给右下角
                matrix[begin + k][end] = matrix[begin][begin + k] # 左上角给右上角
                matrix[begin][begin + k] = temp # 左下角给左上角
        return
        '''
        n = len(matrix)
        # 副对角线
        for i in range(n):
            for j in range(n-i):
                matrix[i][j], matrix[n-1-j][n-1-i] = matrix[n-1-j][n-1-i], matrix[i][j]
        # 水平反转
        for i in range(n//2):
            matrix[i], matrix[n-1-i] = matrix[n-1-i], matrix[i]
        return 


