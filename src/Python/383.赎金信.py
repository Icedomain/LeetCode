#
# @lc app=leetcode.cn id=383 lang=python3
#
# [383] 赎金信
#
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letter_map = {}
        for i in magazine:
            '''
            if i in letter_map:
                letter_map[i] += 1
            else:
                letter_map[i] = 1
            '''
            letter_map[i] = letter_map.get(i, 0) + 1
        for i in ransomNote:
            '''
            if i not in letter_map:
                return False
            else:
                letter_map[i] -= 1
            '''
            letter_map[i] = letter_map.get(i, 0) - 1
            if letter_map[i]<0:
                return False
        return True
        

