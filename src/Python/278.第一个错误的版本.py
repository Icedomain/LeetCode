#
# @lc app=leetcode.cn id=278 lang=python3
#
# [278] 第一个错误的版本
#
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        l ,r = 0 , n-1
        while l <= r:
            mid = (l+r)//2
            if isBadVersion(0) == isBadVersion(mid):
                l = mid + 1
            elif isBadVersion(n) == isBadVersion(mid):
                r = mid -1
        return  l

