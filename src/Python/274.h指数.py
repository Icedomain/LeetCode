#
# @lc app=leetcode.cn id=274 lang=python3
#
# [274] H指数
#
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        i = 0
        while i<len(citations) and citations[len(citations)-1-i]>i:
            i += 1
        return i
