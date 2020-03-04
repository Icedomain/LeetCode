#
# @lc app=leetcode.cn id=151 lang=python3
#
# [151] 翻转字符串里的单词
#

class Solution:
    def reverseWords(self, s: str) -> str:
        if len(s) == 0:
            return s
        
        '''
        temp = s.split(' ')
        temp = [t for t in temp if len(t) > 0]
        temp.reverse()
        return ' '.join(temp)
        '''
        s = s + " "
        l = 0
        stack = []
        for i in range(l,len(s)):
            if s[i] == " " :
                if l != i:
                    stack.append(s[l:i])
                l = i + 1

        stack.reverse()
        return " ".join(stack)


