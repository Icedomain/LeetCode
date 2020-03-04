#
# @lc app=leetcode.cn id=90 lang=python3
#
# [90] 子集 II
#
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        # self.dfs(nums, 0, [], res)
        self.dfs2(nums, 0, [], res)
        return res
    
    def dfs(self, nums, index, path, res):
        if path not in res:
            res.append(path)
        for i in range(index, len(nums)):
            self.dfs(nums, i+1, path+[nums[i]], res)
        
    def dfs2(self, nums, index, path, res):
        res.append(path)
        for i in range(index, len(nums)):
            if i != index and nums[i] == nums[i-1]:
                continue
            self.dfs2(nums, i+1, path+[nums[i]], res)

