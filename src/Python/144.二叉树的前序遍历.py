#
# @lc app=leetcode.cn id=144 lang=python3
#
# [144] 二叉树的前序遍历
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        result = []
        stack = [root]

        while stack:
            p = stack.pop()
            result.append(p.val)
            if p.right:
                stack.append(p.right)
            if p.left:
                stack.append(p.left)
        return result

