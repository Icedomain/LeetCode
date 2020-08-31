#
# @lc app=leetcode.cn id=692 lang=python3
#
# [692] 前K个高频单词
#
import collections
class Solution:
    def topKFrequent2(self, words: List[str], k: int) -> List[str]:
        dict = {}
        for x in words:
            if x in dict:
                dict[x] += 1
            else:
                dict[x] = 1
        res = sorted(dict, key=lambda x: (-dict[x], x))
        return res[:k]

    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dic = dict(collections.Counter(words))
        res = sorted(dic, key=lambda x: (-dic[x], x))
        return res[:k]
