#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        return self.yes(root.left ,root.right)
    
    def yes(self,left,right):
        if left is None and right is None:
            return True
        if left and right and left.val == right.val:
            if self.yes(left.left,right.right) and self.yes(left.right,right.left):
                return True
        return False

