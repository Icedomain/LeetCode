#
# @lc app=leetcode.cn id=367 lang=python3
#
# [367] 有效的完全平方数
#
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        '''
        l,r = 1,num
        while l <= r:
            mid = (l+r)//2
            if mid ** 2 == num:
                return True
            elif mid ** 2 < num:
                l = mid +1
            else:
                r = mid -1
        return False
        '''
        x = num
        while x ** 2 > num:
            x = (x+num//x)//2
        return x ** 2 == num

