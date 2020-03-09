#
# @lc app=leetcode.cn id=344 lang=python3
#
# [344] 反转字符串
#
class Solution:
    def reverseString(self, s: List[str]) -> None:
        n =len(s)
        for i in range(n//2):
            s[i],s[n-i-1] = s[n-i-1],s[i]


