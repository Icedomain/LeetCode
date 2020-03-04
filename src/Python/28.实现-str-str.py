#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 实现 strStr()
#
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle or haystack == needle:
            return 0
        elif len(haystack)<= len(needle):
            return -1
        
        leng = len(needle)
        for i in range(len(haystack)-leng +1):
            if needle == haystack[i:i+leng]:
                return i
        return -1

