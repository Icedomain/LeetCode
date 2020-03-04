#
# @lc app=leetcode.cn id=236 lang=python3
#
# [236] 二叉树的最近公共祖先
#

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #若root为空或者root为p或者root为q,说明找到了p或q其中一个
        if(root is None or root== p or root== q):
            return root        
        
        left  = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right,p,q)

        #若左子树找到了p,右子树找到了q,说明此时的root就是公共祖先
        if left and right :
            return root      
        # 若左子树是none右子树不是，说明右子树找到了p或q
        if not left :    
            return right
        # 同理
        if not right :  
            return left
        return None


