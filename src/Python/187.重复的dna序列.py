#
# @lc app=leetcode.cn id=187 lang=python3
#
# [187] 重复的DNA序列
#
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        dic,res = {}, set()
        for i in range(len(s)-9):
            dic[s[i:i+10]] = dic.get(s[i:i+10], 0)+1
            if dic[s[i:i+10]] > 1:
                res.add(s[i:i+10])
        return list(res)


