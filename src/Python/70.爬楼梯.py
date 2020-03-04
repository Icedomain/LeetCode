#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        # 初始的两个　输入1 or 2 
        a, b = 1, 2
        # 从n大于3开始
        for i in range(2, n):
            b ,a = a+b , b 
        return b
        

