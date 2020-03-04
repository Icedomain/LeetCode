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
        self.pathSum2(root, sum, [], result)
        return result
    
    def pathSum2(self,root,sum,path,result):
        if root is None:
            return
        if root.left is None and root.right is None and sum == root.val: 
            path.append(root.val)
            result.append(path)

        self.pathSum2(root.left,  sum - root.val, path + [root.val], result)
        self.pathSum2(root.right, sum - root.val, path + [root.val], result)

