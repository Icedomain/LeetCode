#
# @lc app=leetcode.cn id=434 lang=python3
#
# [434] 字符串中的单词数
#
class Solution:
    def countSegments(self, s: str) -> int:
        if not s:
            return 0 
        '''
        segment_count = 0
        for i in range(len(s)):
            if i == 0 and s[i] != ' ':
                segment_count = 1
            elif s[i-1] == ' ' and s[i] != ' ':
                segment_count += 1

        return segment_count        
        '''
        s_list = list(s.split(" "))
        s_list = [i for i in s_list if i != " " and i != "" ]
        return len(s_list)

