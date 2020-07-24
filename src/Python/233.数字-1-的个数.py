#
# @lc app=leetcode.cn id=233 lang=python3
#
# [233] 数字 1 的个数
#
class Solution:
    def countDigitOne(self, n: int) -> int:
        '''
        # 方法一
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
        '''

        if n <= 0 :
            return 0
        digit, res = 1, 0
        high, cur, low = n // 10, n % 10, 0
        while high != 0 or cur != 0:
            if cur == 0: 
                res += high * digit
            elif cur == 1: 
                res += high * digit + low + 1
            else: 
                res += (high + 1) * digit
            # 往左移
            low += cur * digit
            cur = high % 10
            high //= 10
            digit *= 10
        return res

