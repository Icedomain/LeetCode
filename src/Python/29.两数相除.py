#
# @lc app=leetcode.cn id=29 lang=python3
#
# [29] 两数相除
#
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if (dividend < 0 and divisor < 0) or (dividend > 0 and divisor > 0):
            positive = 1
        else:
            positive = -1
        
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        # 快除法
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                dividend -= temp
                res += i
                # 除数乘以2 商一下子也多2
                i <<= 1
                temp <<= 1
        
        # 防止溢出
        return min(max(positive * res,-2**31) , 2**31-1)

