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
        if not root:
            return []
        res = []
        self.dfs(root, [] ,res )
        paths = ['->'.join(path) for path in res ]
        return paths

    def dfs(self , node , path ,res):
        # 终止条件 没有子节点
        if not node.left and not node.right:
            res.append(path+[str(node.val)]) 
            return
        path = path + [str(node.val)]
        if node.left:
            self.dfs(node.left  , path , res )
        if node.right:
            self.dfs(node.right , path, res )
        

