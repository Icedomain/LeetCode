#
# @lc app=leetcode.cn id=509 lang=python3
#
# [509] 斐波那契数
#
class Solution:
    def fib(self, N: int) -> int:
        if N < 2:
            return N
        a,b = 0,1
        for _ in range(2,N+1):
            a,b = b,(a+b)%(10**9+7)
        return b

