#
# @lc app=leetcode.cn id=84 lang=python3
#
# [84] 柱状图中最大的矩形
#
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # 此处较为巧妙。若heights数组中元素都是单增序列，则最后无法出栈stack，也就无法计算最大面积，所以补个0，使之最后可以出栈
        heights.append(0)
        stack = [-1]
        res = 0
        
        for idx in range(len(heights)):
            # 不是单调栈
            while heights[stack[-1]] > heights[idx]:
                h = heights[stack.pop()]
                w = idx - stack[-1] - 1
                res = max(res, h*w)
            stack.append(idx)
        return res

