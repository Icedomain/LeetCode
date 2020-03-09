#
# @lc app=leetcode.cn id=383 lang=python3
#
# [383] 赎金信
#
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letter_map = {}
        for i in magazine:
            letter_map[i] = letter_map.get(i, 0) + 1
        for i in ransomNote:
            letter_map[i] = letter_map.get(i, 0) - 1
            if letter_map[i]<0:
                return False
        return True
        

