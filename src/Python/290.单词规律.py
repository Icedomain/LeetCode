#
# @lc app=leetcode.cn id=290 lang=python3
#
# [290] 单词规律
#
class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        word_list = str.split(' ')
        pattern_list = list(pattern)
        if len(word_list) != len(pattern_list):
            return False
        for i, word in enumerate(word_list):
            idx = word_list.index(word)
            idx2 = pattern_list.index(pattern[i])
            if idx != idx2:
                return False            
        return True


