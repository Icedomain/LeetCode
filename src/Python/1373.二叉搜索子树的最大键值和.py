#
# @lc app=leetcode.cn id=1373 lang=python3
#
# [1373] 二叉搜索子树的最大键值和
#

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: TreeNode) -> int:
        self.maxVaL = 0
        self.dfs(root)
        return self.maxVaL
        
    def dfs(self, root):
        # 返回三个变量
        # 分别为【以当前节点为根节点的二叉搜索树的和】,【上界】,【下界】
        if not root:
            return 0, float('inf'), -float('inf') 

        value1, minVaL1, maxVaL1 = self.dfs(root.left)
        value2, minVaL2, maxVaL2 = self.dfs(root.right)     
        # 满足二叉搜索树条件
        if maxVaL1 < root.val and root.val < minVaL2 : 
            cur = value1 + value2 + root.val
            self.maxVaL = max(self.maxVaL, cur )
            return cur , \
                min(minVaL1, root.val), max(maxVaL2, root.val)
        else:
            # 说明该节点无法构成二叉搜索树，返回恒不成立的条件，一直返回到顶
            return root.val, -float('inf'), float('inf')  

