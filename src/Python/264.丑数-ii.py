#
# @lc app=leetcode.cn id=264 lang=python3
#
# [264] 丑数 II
#
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly = [1]
        idx2 = idx3 = idx5 = 0
        i = 1
        while i < n:
            newugly = min(ugly[idx2]*2,ugly[idx3]*3,ugly[idx5]*5)
            ugly.append(newugly)
            while ugly[idx2]*2 <= newugly:
                idx2 += 1
            while ugly[idx3]*3 <= newugly:
                idx3 += 1
            while ugly[idx5]*5 <= newugly:
                idx5 += 1
            i += 1
        return ugly[-1]


