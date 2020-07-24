#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        self.dfs(n,k,1,[],res)
        return res

    def dfs(self,n,k,start,path,res):
        if 0 == k and path not in res:
            res.append(path)
            return
        for i in range(start,n+1):
            self.dfs(n,k-1,i+1,path+[i] ,res)

