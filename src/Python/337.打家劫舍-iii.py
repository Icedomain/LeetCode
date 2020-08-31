#
# @lc app=leetcode.cn id=337 lang=python3
#
# [337] 打家劫舍 III
#

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict
class Solution:
    def rob2(self, root: TreeNode) -> int:
        self.f = defaultdict(int)
        self.g = defaultdict(int)

        self.dfs(root)
        return max(self.f[root] , self.g[root])

    def dfs2(self , o):
        if not o:
            return 
        self.dfs(o.left)
        self.dfs(o.right)

        self.f[o] = o.val + self.g[o.left] + self.g[o.right]
        self.g[o] = max(self.f[o.left], self.g[o.left]) +\
            max(self.f[o.right], self.g[o.right]
            )

    def rob(self, root: TreeNode) -> int:
        selected , notSelected = self.dfs(root)
        return max(selected , notSelected)

    def dfs(self , o):
        if not o:
            return ( 0 , 0 )
        ls , ln = self.dfs(o.left)
        rs , rn = self.dfs(o.right)

        return (
            o.val + ln + rn,
            max( ls,ln ) + max(rs , rn)
        )


