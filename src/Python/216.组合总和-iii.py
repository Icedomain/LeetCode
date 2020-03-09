#
# @lc app=leetcode.cn id=216 lang=python3
#
# [216] 组合总和 III
#
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        self.dfs(k,n,1,[],res)
        return res

    def dfs(self,k,target,start,path,res):
        # 终止条件
        if target == 0 and len(path) == k:
            res.append(path)
            return
        elif target < 0 or len(path) > k or start > 9 :
            return
        
        for i in range(start,10):
            self.dfs(k,target-i,i+1,path+[i],res)

