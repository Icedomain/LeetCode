#
# @lc app=leetcode.cn id=233 lang=python3
#
# [233] 数字 1 的个数
#
class Solution:
    def countDigitOne(self, n: int) -> int:
        res = 0
        a = 1
        b = 1
        while n >= 1:
            # 用(x+8)//10来判断一个数是否大于等于2
            # 从低位到高位
            res += (n + 8)//10*a
            if n % 10 == 1:
                res += b
            b += n % 10 * a
            a *= 10
            n //= 10
        return res

