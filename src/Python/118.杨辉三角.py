#
# @lc app=leetcode.cn id=118 lang=python3
#
# [118] 杨辉三角
#
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # 全部都用1先填充
        out = [[1]*(i+1) for i in range(numRows)]
        for r in range(numRows):
            for col in range(1,r):
                out[r][col] = out[r-1][col-1] + out[r-1][col]
        return out 



