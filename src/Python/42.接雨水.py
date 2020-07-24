#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0 
        l ,r = 0 , len(height) - 1

        res = 0 
        l_max , r_max = 0 , 0
        while l < r :
            if height[l] < height[r]:
                l_max = max(l_max , height[l])
                res += max(0,l_max - height[l])
                l += 1
            else:
                r_max = max(r_max , height[r])
                res += max(0 ,r_max - height[r])
                r -= 1
        return res

