#
# @lc app=leetcode.cn id=214 lang=python3
#
# [214] 最短回文串
#
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        '''
        # 暴力法
        r = s[::-1]
        for i in range(len(s)) :
            if s[0: len(s)-i ] == r[i:] :
                return r[:i] + s
        return ""
        '''
        '''
        # 双指针法
        i = 0
        # 找到从头开始，最长的回文子串
        for j in range(len(s) - 1, -1, -1):
            if s[i] == s[j]: 
                i += 1
        if i == len(s): 
            return s
        # 后缀
        suffix = s[i:]
        return suffix[::-1] + self.shortestPalindrome(s[:i]) + suffix
        '''

        # kmp算法
        table = self.kmp(s + "#" + s[::-1])
        return s[table[-1]:][::-1] + s
        

    def kmp(self,p):
        table = [0] * len(p)
        i = 1
        j = 0
        while i < len(p):
            if p[i] == p[j]:
                j += 1
                table[i] = j
                i += 1
            else :
                if j > 0:
                    j = table[j - 1]
                else:
                    i += 1
                    j = 0
        return table
