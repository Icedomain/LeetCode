#
# @lc app=leetcode.cn id=680 lang=python3
#
# [680] 验证回文字符串 Ⅱ
#
class Solution:
    def validPalindrome(self, s: str) -> bool:
        '''
        # 暴力解 不一样的地方去掉一个看能不能回文
        for i in range(len(s)//2):
            if s[i] != s[-1-i]:
                t, u = s[:i]+s[i+1:], s[:-1-i]+s[len(s)-i:]
                return t == t[::-1] or u == u[::-1]
        return True
        '''

        s = list(s)
        l , r = 0 , len(s) - 1
        while l < r:
            if s[l] != s[r]:
                # 去掉l 或者去掉r 
                # 一个小技巧就是可以忽略两端的元素 因为已经匹配好了
                u ,t = s[l+1:r+1] , s[l:r]
                return t == t[::-1] or u == u[::-1]
            l += 1
            r -= 1
        return True
