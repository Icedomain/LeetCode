#
# @lc app=leetcode.cn id=112 lang=python3
#
# [112] 路径总和
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        
        sum -= root.val
        if sum == 0 and not root.left and not root.right:
            return True
        left = self.hasPathSum(root.left,sum)
        right = self.hasPathSum(root.right,sum)
        return left or right

