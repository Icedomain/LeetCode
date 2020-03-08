#
# @lc app=leetcode.cn id=148 lang=python3
#
# [148] 排序链表
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        fast = slow = head
        pre = None
        while fast and fast.next:
            fast = fast.next.next
            pre = slow
            slow = slow.next
        pre.next = None
        return self.mergeTwoLists(self.sortList(head),self.sortList(slow))
    
    def mergeTwoLists(self, l1, l2):
        res = now = ListNode(-1000)
        while l1 and l2:
            if l1.val <= l2.val:
                now.next = l1
                l1 = l1.next
            else:
                now.next = l2
                l2 = l2.next
            now = now.next
        now.next = l1 or l2
        return res.next
