#
# @lc app=leetcode.cn id=290 lang=python3
#
# [290] 单词规律
#
class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        '''
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
        '''
        
        words = str.split(" ")
        hash_table_pattern = {}
        hash_table_words = {}
        
        if len(words) != len(pattern):
            return False
        #第一步
        for i, letter in enumerate(pattern):
            if letter in hash_table_pattern:
                if hash_table_pattern[letter] != words[i]:
                    return False
            else:
                hash_table_pattern[letter] = words[i]
        #第二步
        for i, word in enumerate(words):
            if word in hash_table_words:
                if hash_table_words[word] != pattern[i]:
                    return False
            else:
                hash_table_words[word] = pattern[i]
        return True
