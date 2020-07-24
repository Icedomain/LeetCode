#
# @lc app=leetcode.cn id=58 lang=python3
#
# [58] 最后一个单词的长度
#
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if not s :
            return 0
        tmp = s.split(' ')
        tmp = [t for t in tmp if len(t) > 0]
        if not tmp:
            return 0
        else:
            return len(tmp[-1])

