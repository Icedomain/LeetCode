#
# @lc app=leetcode.cn id=124 lang=python3
#
# [124] 二叉树中的最大路径和
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.res = -float('inf')
        self.maxend(root)
        return self.res

    def maxend(self,root):
        # 函数返回的是单侧最大值
        if root is None:
            return 0
        left = self.maxend(root.left)
        right = self.maxend(root.right)
        self.res = max(self.res, left + root.val + right)
        return max(root.val + max(left, right), 0)


