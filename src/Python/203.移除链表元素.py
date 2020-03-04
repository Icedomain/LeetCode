#
# @lc app=leetcode.cn id=203 lang=python3
#
# [203] 移除链表元素
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        
        prehead = ListNode(-1)
        prehead.next = head
        last, pos = prehead, head
        while pos is not None:
            if pos.val == val:
                # last 跟上了pos
                last.next = pos.next
            else:
                last = pos
            pos = pos.next
        return prehead.next

