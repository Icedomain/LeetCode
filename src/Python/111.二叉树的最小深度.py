#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth2(self, root: TreeNode) -> int:
        if not root:
            return 0
        elif not root.left:
            return self.minDepth(root.right) + 1
        elif not root.right:
            return self.minDepth(root.left) + 1
        else:
            return min(self.minDepth(root.left) , 
                        self.minDepth(root.right)) + 1


    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        result = float('inf')
        q = [(root, 1)]
        while q:
            node, depth = q.pop(0)
            if not node.left and not node.right:
                result = min(result, depth)
                
            if node.left:
                q.append((node.left, depth + 1))

            if node.right:
                q.append((node.right, depth + 1))

        return result
