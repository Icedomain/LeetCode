#
# @lc app=leetcode.cn id=116 lang=python3
#
# [116] 填充每个节点的下一个右侧节点指针
#
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None or root.left is None:
            return root
        # 左右链接
        root.left.next = root.right
        if root.next :
            root.right.next = root.next.left
        else:
            root.right.next = None
        
        self.connect(root.left)
        self.connect(root.right)

        return root

