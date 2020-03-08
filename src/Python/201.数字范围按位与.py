#
# @lc app=leetcode.cn id=201 lang=python3
#
# [201] 数字范围按位与
#
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        '''
        # 时间溢出
        res = m
        for i in range(m+1,n+1):
            res = res & i
            if res == 0 :
                break
        return res
        '''

        i = 0
        while m != n:
            m >>= 1
            n >>= 1
            i += 1
        return m << i


