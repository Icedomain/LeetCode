#
# @lc app=leetcode.cn id=226 lang=python3
#
# [226] 翻转二叉树
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        root.left ,root.right = self.invertTree(root.right) ,self.invertTree(root.left)
        return root

