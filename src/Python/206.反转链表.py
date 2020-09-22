#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList2(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        cur = head
        prev = None
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        return prev

    def reverseList(self, head: ListNode) -> ListNode:
        # 递归方法
        if not head or not head.next:
            return head
        headNode = self.reverseList(head.next)
        # head headNode 顺序(环)
        head.next.next = head
        # head headNode head(断开)
        head.next = None
        return headNode

