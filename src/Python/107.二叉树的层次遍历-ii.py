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
        '''
        if root is None:
            return []
        # use stack
        stack = [[root]]
        res = []
        while len(stack) > 0:
            # 取出最新装入的list
            top = stack.pop()
            # 一直在头部插入以达到倒序
            res.insert(0, [t.val for t in top])
            # 向下新一轮扫描
            temp = []
            for node in top:
                if node.left is not None:
                    temp.append(node.left)
                if node.right is not None:
                    temp.append(node.right)
            if len(temp) > 0:
                stack.append(temp)
        return res
        '''
        
        # 递归法
        if root is None:
            return None
        result = [[]]
        self.traverse(root,1,result)
        return reversed(result)

    def traverse(self,root,level,result):
        if root is None:
            return
        if level > len(result):
            result.append([])
        result[level-1].append(root.val)
        self.traverse(root.left,level+1,result)
        self.traverse(root.right,level+1,result)




