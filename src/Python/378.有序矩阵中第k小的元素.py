#
# @lc app=leetcode.cn id=378 lang=python3
#
# [378] 有序矩阵中第K小的元素
#

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        left, right = matrix[0][0], matrix[-1][-1]
        while left < right:
            mid = (left + right) // 2
            if self.check(matrix,k, mid):
                right = mid
            else:
                left = mid + 1
        return left

    def check(self,matrix ,k,  mid):
        # res 记录左上角的个数
        row, col = len(matrix) - 1, 0
        res = 0
        while row >= 0 and col < len(matrix):
            if matrix[row][col] <= mid:
                res += (row + 1)
                col += 1
            else:
                row -= 1
        return res >= k
