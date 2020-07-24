#
# @lc app=leetcode.cn id=113 lang=python3
#
# [113] 路径总和 II
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        res = []
        self.dfs(root , sum ,[],res)
        return res

    def dfs(self,root ,sum ,path,res):
        if not root:
            return
        # 这里判断不能是sum==0 和root是None 
        # 因为可能是单侧有节点的情况 这样子不是支路 但是可以返回 矛盾了
        elif sum == root.val and (not root.left) and (not root.right) :
            res.append(path+[root.val])
            return
        self.dfs(root.left , sum - root.val ,path + [root.val],res)
        self.dfs(root.right ,sum - root.val ,path + [root.val],res)

