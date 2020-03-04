#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        self.dfs(candidates, target, 0, [], res)
        return res
        
    def dfs(self, nums, target, index, path, res):
        if target < 0:
            return
        if target == 0:
            res.append(path)
            return 
        for i in range(index, len(nums)):
            self.dfs(nums, target-nums[i], i, path+[nums[i]], res)

