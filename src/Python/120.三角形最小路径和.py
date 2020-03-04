#
# @lc app=leetcode.cn id=120 lang=python3
#
# [120] 三角形最小路径和
#
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return 
        # 倒数第二行到最上面一行
        for i in range( len(triangle)-2, -1, -1):
            # 每行的第一列到最后一列
            for j in range(len(triangle[i])):
                triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])
        return triangle[0][0]

