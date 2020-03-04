#
# @lc app=leetcode.cn id=257 lang=python3
#
# [257] 二叉树的所有路径
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if root is None:
            return []
        paths = []
        # 路径　节点　现有的子路
        self.getpath(paths , root, [])
        res = ['->'.join(path) for path in paths]
        return res

    def getpath(self , res , node , path ):
        # 没有左右子树
        if node.left is None and node.right is None:
            res.append(path + [str(node.val)]) 
            return
        # 否则
        path = path + [str(node.val)]
        if node.left is not None:
            self.getpath(res ,node.left ,path  )
        if node.right is not None:
            self.getpath(res ,node.right ,path  )
        

