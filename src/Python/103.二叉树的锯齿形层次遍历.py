#
# @lc app=leetcode.cn id=103 lang=python3
#
# [103] 二叉树的锯齿形层次遍历
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root :
            return []
        result = [[]]
        self.traverse(root,0,result,True)
        return result

    def traverse(self,root,level,result,flag):
        if root is None:
            return
        if level >= len(result):
            result.append([])
        
        if flag:
            result[level].append(root.val)
        else:
            result[level].insert(0,root.val)
        self.traverse(root.left,level+1,result, not flag)
        self.traverse(root.right,level+1,result, not flag)

