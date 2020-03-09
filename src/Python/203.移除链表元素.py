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
        prev, curr = dummy, head
        while curr :
            if curr.val == val:
                # prev 跟上了curr
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        return dummy.next

