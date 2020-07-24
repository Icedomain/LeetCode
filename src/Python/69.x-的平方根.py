#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根
#
class Solution:
    def mySqrt(self, x: int) -> int:
        l ,r = 0 , x
        while l <= r:
            mid = (l+r)//2
            if mid**2 <= x < (mid+1)**2:
                return mid
            elif x < mid**2:
                r = mid
            else:
                l = mid + 1

