#
# @lc app=leetcode.cn id=1147 lang=python3
#
# [1147] 段式回文
#
class Solution:
    def longestDecomposition(self, text: str) -> int:
        n = len(text)
        i, j = 0, n - 1
        str1, str2, res = '', '', 0
        while i < j:
            str1 = str1 + text[i]
            str2 = text[j] + str2
            if str1 == str2:
                res += 2
                str1, str2 = '', ''
            i += 1
            j -= 1
        # 奇或者中间那段
        if n % 2 == 1 or str1 != '':
            res += 1
        return res

