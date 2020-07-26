#
# @lc app=leetcode.cn id=129 lang=python3
#
# [129] 求根到叶子节点数字之和
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        return self.sum_tree(root,0)

    def sum_tree(self,root,sum):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return sum*10+root.val

        return  self.sum_tree(root.left,sum*10+root.val) +\
                self.sum_tree(root.right,sum*10+root.val)

