#
# @lc app=leetcode.cn id=230 lang=python3
#
# [230] 二叉搜索树中第K小的元素
#

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        '''
        # 方法一
        reslist = self.inorder(root)
        return reslist[k - 1]
        '''
        # 方法二
        # 左子树有多少个点
        n = self.count(root.left)
        if n == k -1 :
            return root.val
        # 递归到左子树
        elif n > k - 1:
            return self.kthSmallest(root.left,k)
        # 递归到右子树
        else:
            return self.kthSmallest(root.right,k-1-n)

    def inorder(self,r):
        if r:
            return self.inorder(r.left) + [r.val] + self.inorder(r.right)  
        else:
            return []

    def count(self,root):
        if not root :
            return 0 
        return self.count(root.left) + self.count(root.right) + 1

