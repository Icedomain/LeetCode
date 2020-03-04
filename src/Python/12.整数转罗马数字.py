#
# @lc app=leetcode.cn id=12 lang=python3
#
# [12] 整数转罗马数字
#
class Solution:
    def intToRoman(self, num: int) -> str:
        # 贪心算法
        dic = {
            'M': 1000,
            'CM': 900, 'D': 500, 'CD': 400, 'C': 100,
            'XC': 90, 'L': 50, 'XL': 40, 'X': 10,
            'IX': 9, 'V': 5, 'IV': 4, 'I': 1,
        }
        result = ""       
        for letter,number in dic.items():
            if num >= number:
                result += letter*(num//number)
                num %= number
        return result
