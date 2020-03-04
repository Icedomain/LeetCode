#
# @lc app=leetcode.cn id=566 lang=python3
#
# [566] 重塑矩阵
#
class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        row = len(nums)
        col = len(nums[0])
        if row * col != r*c:
            return nums            
        res = [[]]
        for i in range(row):
            for j in range(col):
                k = nums[i][j]
                if len(res[-1]) < c:
                    res[-1].append(k)
                else:
                    res.append([k])
        return res
        


