#
# @lc app=leetcode.cn id=387 lang=python3
#
# [387] 字符串中的第一个唯一字符
#
class Solution:
    def firstUniqChar(self, s: str) -> int:
        letter_map = {}
        for i in s:
            letter_map[i] = letter_map.get(i, 0) + 1
        for i in range(len(s)):
            if letter_map[s[i]] == 1:
                return i
        return -1
