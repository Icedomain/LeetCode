#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left,right = 0,len(height) - 1
        while left < right :
            # 高取左边和右边的高当中的最小值， 下标right-left为宽，两者相乘为面积
            temp = min(height[left], height[right]) * (right - left)
            max_area = max(max_area, temp)
            # 判断哪条高小，小的那边下标进行操作
            if height[right] > height[left]:
                left += 1
            else:
                right -= 1
        return max_area


