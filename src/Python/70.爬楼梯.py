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
        for _ in range(3, n+1):
            b ,a = a + b , b 
        return b

