#
# @lc app=leetcode.cn id=50 lang=python3
#
# [50] Pow(x, n)
#
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n < 0:
            return 1 / self.myPow(x, -n)
        # 奇数
        elif n & 1 :
            return x * self.myPow(x, n-1)
        else:
            return self.myPow(x*x, n // 2)
        
    def myPow2(self, x: float, n: int) -> float:
        if x == 0: 
            return 0
        if n == 0:
            return 1
        elif n < 0:
            x, n = 1 / x, -n
        
        res = 1
        while n:
            # 奇数
            if n & 1 :
                res *= x
            x *= x
            n >>= 1
        return res
