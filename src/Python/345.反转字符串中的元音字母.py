#
# @lc app=leetcode.cn id=345 lang=python3
#
# [345] 反转字符串中的元音字母
#
class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        n =len(s)
        l ,r = 0,n-1
        while l < r:
            if s[l] not in 'aeiouAEIOU':
                l += 1
            elif s[r] not in 'aeiouAEIOU':
                r -= 1
            else:
                s[l],s[r] = s[r],s[l]
                l += 1
                r -= 1
        return ''.join(s)



