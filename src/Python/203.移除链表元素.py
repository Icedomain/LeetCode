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
        dummy = ListNode(-1)
        dummy.next = head
        prev, cur = dummy, head
        while cur :
            if cur.val == val:
                # prev 跟上了cur
                prev.next = cur.next
            else:
                prev = cur
            cur = cur.next
        return dummy.next

