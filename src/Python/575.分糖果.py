#
# @lc app=leetcode.cn id=575 lang=python3
#
# [575] 分糖果
#
class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        return int(min( len(set(candies)) , len(candies)//2))

