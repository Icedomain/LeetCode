#
# @lc app=leetcode.cn id=223 lang=python3
#
# [223] 矩形面积
#
class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        x = min( C,G )- max(A,E)
        y = min( D,H )- max(B,F)
        return (A-C)*(B-D) + (E-G)*(F-H) - max(x,0)*max(y,0) 

