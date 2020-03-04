#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dmap = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
        }
        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return list(dmap[digits])
        prev = self.letterCombinations(digits[:-1])
        additional = dmap[digits[-1]]
        return [s + c for s in prev for c in additional]
        

