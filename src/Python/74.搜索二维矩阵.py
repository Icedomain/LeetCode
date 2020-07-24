#
# @lc app=leetcode.cn id=74 lang=python3
#
# [74] 搜索二维矩阵
#
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:   
        if len(matrix)==0 or len(matrix[0])==0 or target < matrix[0][0] or target > matrix[-1][-1]:
            return False
        row = 0
        col = len(matrix[0]) -1
        while row < len(matrix) and col >= 0 :
            if matrix[row][col] > target:
                col -= 1
            elif matrix[row][col] < target:
                row += 1
            else :
                return True
        return False

