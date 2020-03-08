#
# @lc app=leetcode.cn id=95 lang=python3
#
# [95] 不同的二叉搜索树 II
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            return []
        return self.get_trees(1,n)

    def get_trees(self,start,end):
        res = []
        if start > end:
            # 空子树情况
            return [None]
        for i in range(start,end+1):
            lefts = self.get_trees(start,i-1)
            rights = self.get_trees(i+1,end)
            # lefts 和 rights 有可能是空的[None]
            for l in lefts:
                for r in rights:
                    root = TreeNode(i)
                    root.left = l
                    root.right = r
                    res.append(root)
        return res
        

