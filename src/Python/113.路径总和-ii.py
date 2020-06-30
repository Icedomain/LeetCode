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
        if root is None:
            return []
        result = []
        self.dfs(root, sum, [], result)
        return result
    
    def dfs(self,root,sum,path,result):
        if root is None:
            return
        if root. left is None and root.right is None and sum == root.val:
            path.append(root.val)
            result .append(path)
            
        self.dfs(root.left,  sum - root.val, path + [root.val], result)
        self.dfs(root.right, sum - root.val, path + [root.val], result)

