#
# @lc app=leetcode.cn id=114 lang=python3
#
# [114] 二叉树展开为链表
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        if root is None:
            return 

        self.flatten(root.left)
        self.flatten(root.right)

        if root.left is None:
            return

        # 左子树插到root和root.right之间
        p = root.left
        # 左子链的最后一个节点
        while p.right:
            p = p.right
        p.right = root.right
        root.right = root.left
        root.left = None



