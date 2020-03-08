#
# @lc app=leetcode.cn id=117 lang=python3
#
# [117] 填充每个节点的下一个右侧节点指针 II
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
        head = root
        dummy = Node(-1)
        prev = dummy
        # dummy 当前行的最左端节点
        while root :
            if root.left :
                prev.next = root.left
                prev = prev.next
            if root.right :
                prev.next = root.right
                prev = prev.next
            root = root.next
            # 行的尾部
            if root is None:
                # dummy.next为前面prev.next 第一次赋值的节点
                root = dummy.next
                #前面链接断开,开始新的一行
                dummy.next = None
                # prev值新的
                prev = dummy
        return head

