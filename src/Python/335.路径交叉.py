#
# @lc app=leetcode.cn id=335 lang=python3
#
# [335] 路径交叉
#
class Solution:
    def isSelfCrossing(self, x: List[int]) -> bool:
        for i in range(len(x)):
            if i + 3 < len(x) and x[i] >= x[i + 2] \
                and x[i + 1] <= x[i + 3]:
                return True
            if i + 4 < len(x) and x[i + 1] == x[i + 3] \
                and x[i] + x[i + 4] >= x[i + 2]:
                return True
            if i + 5 < len(x) and x[i] < x[i + 2] \
                and x[i + 4] < x[i + 2]     \
                and x[i + 2] <= x[i] + x[i + 4]  \
                and x[i + 1] < x[i + 3] \
                and x[i + 3] <= x[i + 1] + x[i + 5]:
                return True
        return False

