#
# @lc app=leetcode.cn id=557 lang=python3
#
# [557] 反转字符串中的单词 III
#
class Solution:
    def reverseWords2(self, s: str) -> str:
        return ' '.join([word[::-1] for word in s.split(' ')])

    def reverseWords(self, s: str) -> str:
        s = list(s)
        s.append(' ')
        l = 0
        for i in range(len(s)):
            if s[i] == " ":
                self.rever(s,l,i-1)
                l = i + 1
        return ''.join(s[:-1])

    def rever(self,s,l,r):
        while l < r:
            s[l],s[r] = s[r],s[l]
            l += 1
            r -= 1
