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
        if not head:
            return None
        # 复制next部分
        cur = head
        while cur :
            nexttmp = cur.next
            node = Node(cur.val)
            node.next = nexttmp
            cur.next = node
            cur = nexttmp
        # 复制random部分
        cur = head
        while cur :
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next
        # 拆分两个单链表
        cur = head
        pnew = res = head.next
        while pnew.next:
            cur.next = pnew.next
            cur = cur.next
            pnew.next = cur.next
            pnew = pnew.next
        pnew.next = None
        cur.next = None
        return res
