#
# @lc app=leetcode.cn id=119 lang=python3
#
# [119] 杨辉三角 II
#
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        '''
        if rowIndex == 0:
            return [1]
        rowIndex += 1
        # 全部都用1先填充
        out = [[1]*(i+1) for i in range(rowIndex)]
        for r in range(rowIndex):
            for col in range(1,r):
                out[r][col] = out[r-1][col-1] + out[r-1][col]
        return out[-1]
        '''
        # 先用1填充
        res = [1]*(rowIndex+1)
        # 从后往前,从上往下覆盖
        for r in range(2,rowIndex+1):
            for col in range(r-1,0,-1):# 逆序
                res[col] += res[col-1]
        return res
