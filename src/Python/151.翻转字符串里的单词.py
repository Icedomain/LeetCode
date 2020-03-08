#
# @lc app=leetcode.cn id=151 lang=python3
#
# [151] 翻转字符串里的单词
#
class Solution:
    def reverseWords(self, s: str) -> str:
        if not s:
            return s
        
        '''
        temp = s.split(' ')
        temp = [t for t in temp if len(t) > 0]
        temp.reverse()
        return ' '.join(temp)
        '''
        s = s + " "
        l = 0
        res = []
        for i in range(l,len(s)):
            if s[i] == " " :
                if l != i:
                    res.append(s[l:i])
                l = i + 1

        res.reverse()
        return " ".join(res)

