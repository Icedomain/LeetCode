#
# @lc app=leetcode.cn id=240 lang=python3
#
# [240] 搜索二维矩阵 II
#
class Solution:
    def searchMatrix(self, matrix, target):
        if not len(matrix) or not len(matrix[0]):
            return False
        # 左下角
        r , c = len(matrix) - 1 , 0 
        while r >= 0 and c < len(matrix[0]):
            if matrix[r][c] > target :
                # 往上
                r -= 1
            elif matrix[r][c] < target :
                # 往右
                c += 1
            else:
                return True
        return False

