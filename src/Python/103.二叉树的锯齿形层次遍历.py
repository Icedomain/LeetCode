#
# @lc app=leetcode.cn id=103 lang=python3
#
# [103] 二叉树的锯齿形层次遍历
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root :
            return []
        result = [[]]
        self.dfs(root,0,result,True)
        return result

    def dfs(self,root,level,result,flag):
        if root is None:
            return
        if level >= len(result):
            result.append([])
        
        if flag:
            result[level].append(root.val)
        else:
            result[level].insert(0,root.val)
        self.dfs(root.left,level+1,result, not flag)
        self.dfs(root.right,level+1,result, not flag)

    # bfs
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        queue = [root]
        res = []
        depth = 1
        while queue:
            size = len(queue)
            level = []
            for _ in range(size):
                cur = queue.pop(0)
                if not cur:
                    continue
                # 奇数正向　偶数反向
                if depth % 2:
                    level.append(cur.val)
                else:
                    level.insert(0,cur.val)
                queue.append(cur.left)
                queue.append(cur.right)
            if level:
                res.append(level)
            depth += 1
        return res


