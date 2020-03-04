#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        prev = dummy = ListNode(-1)
        dummy.next = head
        while prev.next and prev.next.next :
            # prev a b -> prev b a (交换a,b)
            a = prev.next
            b = prev.next.next
            prev.next, b.next, a.next = b, a, b.next
            prev = a
        return dummy.next

