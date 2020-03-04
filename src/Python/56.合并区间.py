#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals
        res = []
        intervals.sort(key = lambda x: x[0])
        s , e = intervals[0][0] , intervals[0][1]

        for i in range(1,len(intervals)):
            # 后边跟着的区间和[s,e]的交叉,相当于合并
            if e >= intervals[i][0] :
                e = max( e , intervals[i][1] )
            # 紧跟着的区间在[s,e]后面
            else:
                res.append([s,e])
                s ,e = intervals[i][0] , intervals[i][1]
        res.append([s,e])
        return res
