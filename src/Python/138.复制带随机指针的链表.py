#
# @lc app=leetcode.cn id=138 lang=python3
#
# [138] 复制带随机指针的链表
#
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None:
            return None
        # 复制next部分
        headcopy = head
        while headcopy:
            node = Node(headcopy.val)
            node.next = headcopy.next
            headcopy.next = node
            headcopy = node.next
        # 复制random部分
        headcopy = head
        while headcopy:
            if headcopy.random:
                headcopy.next.random = headcopy.random.next
            headcopy = headcopy.next.next

        # 拆分两个单链表
        src = head
        pnew = res = head.next

        while pnew.next:
            src.next = pnew.next
            src = src.next
            pnew.next = src.next
            pnew = pnew.next
        src.next = None
        pnew.next = None

        return res

