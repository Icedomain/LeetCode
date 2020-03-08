#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.isOK(root,-float('inf'),float('inf'))

    def isOK(self,root,low,upper):
        if root is None:
            return True
        elif root.val > low and root.val < upper :
            return self.isOK(root.left,low,root.val) and self.isOK(root.right,root.val,upper)
        else:
            return False

