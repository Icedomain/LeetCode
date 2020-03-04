#
# @lc app=leetcode.cn id=219 lang=python3
#
# [219] 存在重复元素 II
#
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic = {}
        for key ,val in enumerate(nums):
            if val in dic and key - dic[val]<=k :
                return True
            dic[val] = key
        return False



