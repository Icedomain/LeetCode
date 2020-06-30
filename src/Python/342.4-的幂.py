#
# @lc app=leetcode.cn id=342 lang=python3
#
# [342] 4的幂
#
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        # bin(4**0) '0b1'
        # bin(4**1) '0b100'
        # bin(4**2) '0b10000'
        # bin(4**3) '0b1000000'
        
        # return num > 0 and num & (num-1) == 0 and len(bin(num)[3:]) % 2 == 0   

        while num > 1:
            num /= 4
        if num == 1:
            return True
        else:
            return False
