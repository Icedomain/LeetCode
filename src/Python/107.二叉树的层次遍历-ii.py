#
# @lc app=leetcode.cn id=107 lang=python3
#
# [107] 二叉树的层次遍历 II
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        # use stack  , only list
        # bfs 
        stack = [root]
        res = []
        while stack:
            # 一直在头部插入以达到倒序
            res.insert(0, [t.val for t in stack])
            # 向下新一轮扫描
            temp = []
            for node in stack:
                if node.left :
                    temp.append(node.left)
                if node.right :
                    temp.append(node.right)
            # update
            stack = temp
        return res
        '''
        # 递归法
        if not root:
            return []
        result = [[]]
        self.traverse(root,0,result)
        result.reverse()
        return result
        '''

    def traverse(self,root,level,result):
        if root is None:
            return
        if level >= len(result):
            result.append([])
        result[level].append(root.val)
        self.traverse(root.left,level+1,result)
        self.traverse(root.right,level+1,result)


