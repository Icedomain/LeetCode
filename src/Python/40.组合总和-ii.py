#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
#
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()                      
        res = []
        self.dfs(candidates,target, 0, [], res)
        return res
        
    def dfs(self, nums,target, start, path, res):
        # 超过了
        if target < 0:
            return
        if target == 0 :
            res.append(path)
            return
        for i in range(start, len(nums)):
            # 解集不重复
            if i > start and nums[i] == nums[i - 1]:
                continue
            self.dfs(nums,target - nums[i],
                    i + 1, path + [nums[i],], res)

