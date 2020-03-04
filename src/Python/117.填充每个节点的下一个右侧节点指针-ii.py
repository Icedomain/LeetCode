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
        dummyHead = Node(-1)
        pre = dummyHead
        # dummyHead 当前行的最左端节点
        while root :
            if root.left :
                pre.next = root.left
                pre = pre.next
            if root.right :
                pre.next = root.right
                pre = pre.next
            root = root.next
            # 行的尾部
            if root is None:
                # pre值新的
                pre = dummyHead
                # dummyHead.next为前面pre.next 第一次赋值的节点
                root = dummyHead.next
                #前面链接断开,开始新的一行
                dummyHead.next = None
        return head




