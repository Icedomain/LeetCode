#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#
class Solution:
    def romanToInt(self, s: str) -> int:
        dicts = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        data = 0
        for item in s:
            data += dicts[item]
        return data        
        

