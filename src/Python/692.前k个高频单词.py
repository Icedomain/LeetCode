#
# @lc app=leetcode.cn id=692 lang=python3
#
# [692] 前K个高频单词
#
import collections
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dic = {}
        for x in words:
            if x in dic:
                dic[x] += 1
            else:
                dic[x] = 1
        res = sorted(dic, key=lambda x: (-dic[x], x))
        return res[:k]

    def topKFrequent2(self, words: List[str], k: int) -> List[str]:
        dic = dict(collections.Counter(words))
        res = sorted(dic, key=lambda x: (-dic[x], x))
        return res[:k]
