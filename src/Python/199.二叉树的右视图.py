#
# @lc app=leetcode.cn id=199 lang=python3
#
# [199] 二叉树的右视图
#

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        res = []
        self.dfs(root, 0,res)
        return res

    def dfs(self,root, depth,res):
        if not root:
            return 
        if depth >= len(res) :
            res.append(0)
        res[depth] = root.val
        # 先进行左子树的迭代,右子树迭代出来的值会覆盖到之前的上面去
        self.dfs(root.left, depth + 1,res)
        self.dfs(root.right, depth + 1,res)
