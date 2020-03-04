#
# @lc app=leetcode.cn id=8 lang=python3
#
# [8] 字符串转换整数 (atoi)
#
class Solution:
    def myAtoi(self, str: str) -> int:
        # 去空格
        str = str.strip()
        if len(str) == 0:
            return 0
        sign = 1
        if str[0] == '+' or str[0] == '-':
            if str[0] == '-':
                sign = -1
            str = str[1:]
        res = 0
        for char in str:
            if char >= '0' and char <= '9':
                res = res * 10 + ord(char) - ord('0')
            if char < '0' or char > '9':
                break
        return max(-2**31, min(sign * res,2**31-1))



