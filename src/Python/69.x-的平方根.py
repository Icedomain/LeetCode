#
# @lc app=leetcode.cn id=69 lang=python
#
# [69] x 的平方根
#
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """       
        l = 0
        r = x
        while l <= r:
            mid = (l+r)//2
            if mid**2 <= x < (mid+1)**2:
                return mid
            elif x < mid**2:
                r = mid
            else:
                l = mid+1
       

