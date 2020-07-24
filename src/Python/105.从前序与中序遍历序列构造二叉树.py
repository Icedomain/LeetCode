#
# @lc app=leetcode.cn id=105 lang=python3
#
# [105] 从前序与中序遍历序列构造二叉树
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not inorder:
            return None
        # 前序的头就是root
        # 中序中,root左边就是左子树,右边是右子树
        val = preorder.pop(0)
        root = TreeNode(val)
        idx = inorder.index(val)
        # 递归构造子树先left后right
        root.left = self.buildTree(preorder, inorder[0:idx])
        root.right = self.buildTree(preorder, inorder[idx+1:])
        return root

