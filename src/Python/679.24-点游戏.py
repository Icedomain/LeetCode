#
# @lc app=leetcode.cn id=679 lang=python3
#
# [679] 24 点游戏
#

class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        if not nums:
            return False
        return self.dfs(nums)
    
    # 四个数取出两个数之后,做加减乘除处理之后加入到原数组中会剩下三个数,递归交给下一层去处理
    def dfs(self,nums):
        if len(nums) == 1: 
            return abs(nums[0]-24) < 1e-6
        # 两个取出后 剩下放回去
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                newnums = [nums[k] for k in range(len(nums)) if i != k and k != j]
                # 加减乘除
                if  self.dfs(newnums + [nums[i]+nums[j]]) or \
                    self.dfs(newnums + [nums[i]*nums[j]]) or \
                    self.dfs(newnums + [nums[i]-nums[j]]) or \
                    self.dfs(newnums + [nums[j]-nums[i]]) or \
                    ( nums[j] != 0 and  self.dfs(newnums + [nums[i]/nums[j]]) ) or \
                    ( nums[i] != 0 and  self.dfs(newnums + [nums[j]/nums[i]]) ):
                    return True
        return False

