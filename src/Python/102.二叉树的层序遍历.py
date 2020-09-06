#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层次遍历
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder2(self, root: TreeNode) -> List[List[int]]:
        if not root :
            return []
        result = [[]]
        self.dfs(root,0,result)
        return result

    def dfs(self,root,level,result):
        if not root:
            return
        if level >= len(result):
            result.append([])
        result[level].append(root.val)
        self.dfs(root.left,level+1,result)
        self.dfs(root.right,level+1,result)

    # bfs
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        queue = [root]
        res = []
        while queue:
            size = len(queue)
            level = []
            for _ in range(size):
                cur = queue.pop(0)
                if not cur:
                    continue
                level.append(cur.val)
                queue.append(cur.left)
                queue.append(cur.right)
            if level:
                res.append(level)
        return res

