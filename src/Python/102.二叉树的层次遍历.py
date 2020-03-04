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
        if root is None:
            return None
        result = [[]]
        self.traverse(root,1,result)
        return result

    def traverse(self,root,level,result):
        if root is None:
            return
        if level > len(result):
            result.append([])
        result[level-1].append(root.val)
        self.traverse(root.left,level+1,result)
        self.traverse(root.right,level+1,result)

        

