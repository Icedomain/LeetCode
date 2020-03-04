#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 :
            return False
        # 最高位的位数
        d = 1
        while x // d >= 10:
            d *= 10
        while x > 0:
            # p q 对应最高位和最低位
            p = x //d 
            q = x % 10
            if p != q :
                return False
            # x 去掉最高位,去掉最低位
            x = x % d // 10 
            # x 去掉了两位,d也减两位
            d //= 100
        return True

