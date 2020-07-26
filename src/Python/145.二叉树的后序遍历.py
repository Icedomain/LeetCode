#
# @lc app=leetcode.cn id=145 lang=python3
#
# [145] 二叉树的后序遍历
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        result = []
        stack = [root]

        while stack:
            p = stack.pop()
            result.append(p.val)
            if p.left :                
                stack.append(p.left)
            if p.right:
                stack.append(p.right)
        return result[::-1]

