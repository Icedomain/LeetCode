#
# @lc app=leetcode.cn id=532 lang=python3
#
# [532] 数组中的K-diff数对
#
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:

        c = collections.Counter(nums)
        dui = 0

        if k < 0 :
            return 0
        elif k == 0 :
            for i in c.keys():
                if c[i]>1:
                    dui += 1
        else:
            for i in c.keys():
                if i + k in c:
                    dui +=1
        return dui


