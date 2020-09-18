#
# @lc app=leetcode.cn id=662 lang=python3
#
# [662] 二叉树最大宽度
#

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree2(self, root: TreeNode) -> int:
        # node pos 
        queue = [(root,0)]
        res = 0
        while queue:
            arr = []
            n = len(queue)
            for _ in range(n):
                node,pos = queue.pop(0)
                arr.append(pos)
                if node.left:
                    queue.append((node.left,pos*2))
                if node.right:
                    queue.append((node.right,pos*2+1))
            res = max(res,1+arr[-1]-arr[0])
        return res

    def widthOfBinaryTree(self, root: TreeNode) -> int:
        self.res = 0
        self.dic = {}
        self.dfs(root , 0 ,0)
        return self.res

    def dfs(self, node, depth, pos):
        if node:
            self.dic.setdefault(depth, pos)
            self.res = max(self.res, pos - self.dic[depth] + 1)
            
            self.dfs(node.left , depth + 1, pos * 2)
            self.dfs(node.right, depth + 1, pos * 2 + 1)

