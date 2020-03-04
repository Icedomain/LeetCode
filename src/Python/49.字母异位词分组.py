#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        # key是单词对应的元素
        # value是字符串
        for word in strs:
            key = ''.join(sorted(word))
            if key not in dic :
                dic[key] = []
            dic[key].append(word)
        res = []
        for i in dic:
            res.append(dic[i])
        return res

