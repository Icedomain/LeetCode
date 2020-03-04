#
# @lc app=leetcode.cn id=57 lang=python3
#
# [57] 插入区间
#
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        s, e = newInterval[0], newInterval[1]
        left, right = [], []
        for inter in intervals:
            # 左边部分
            if s > inter[1]:
                left.append(inter)
            # 右边部分
            elif e < inter[0]:
                right.append(inter)
            # 和区间交叉部分,合并
            else:
                s = min(s, inter[0])
                e = max(e, inter[1])
        return left + [[s, e]] + right  


