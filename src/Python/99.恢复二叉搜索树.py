#
# @lc app=leetcode.cn id=99 lang=python3
#
# [99] 恢复二叉搜索树
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        cur, pre = root, None
        first, second = None, None
        stack = []
        
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:        
                node = stack.pop()
                if pre and pre.val >= node.val:
                    if not first:
                        first = pre
                    second = node
                    
                pre = node
                cur = node.right
        
        first.val, second.val = second.val, first.val
        '''
        # 定义
        self.pre = None
        self.m1, self.m2 = None, None

        self.inorderTraversal(root)
        self.m1.val, self.m2.val = self.m2.val, self.m1.val
        '''

    # 中序遍历
    def inorderTraversal(self, root):
        if root :
            self.inorderTraversal(root.left)
            if self.pre and self.pre.val > root.val:
                if self.m1 == None:
                    self.m1 = self.pre
                self.m2 = root
            self.pre = root
            self.inorderTraversal(root.right)
