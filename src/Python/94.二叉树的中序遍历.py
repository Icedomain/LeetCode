#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        
        result = []
        stack = []
        p = root
        while stack or p:
            # 先把左边的压进去
            if p:
                stack.append(p)
                p = p.left
            # 没有了之后 压右树
            else:
                p = stack.pop()
                result.append(p.val)
                p = p.right
        return result
        
        # return self.inorder(root)

    def inorder(self,r):
        if r:
            return self.inorder(r.left) + [r.val] + self.inorder(r.right)  
        else:
            return []

