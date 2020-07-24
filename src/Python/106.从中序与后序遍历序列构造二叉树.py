#
# @lc app=leetcode.cn id=106 lang=python3
#
# [106] 从中序与后序遍历序列构造二叉树
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder :
            return None
        # 后序的尾部就是root
        # 中序中,root值左边就是左子树,右边是右子树
        val = postorder.pop()
        root = TreeNode(val)
        idx = inorder.index(val)            
        # 递归构造子树先right后left
        root.right = self.buildTree(inorder[idx+1:],postorder)
        root.left  = self.buildTree(inorder[0:idx],postorder)
        return root

