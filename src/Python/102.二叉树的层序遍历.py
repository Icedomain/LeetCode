#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层次遍历
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root :
            return []
        result = [[]]
        self.traverse(root,0,result)
        return result

    def traverse(self,root,level,result):
        if not root:
            return
        if level >= len(result):
            result.append([])
        result[level].append(root.val)
        self.traverse(root.left,level+1,result)
        self.traverse(root.right,level+1,result)

