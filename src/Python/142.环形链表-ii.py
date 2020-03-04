#
# @lc app=leetcode.cn id=142 lang=python3
#
# [142] 环形链表 II
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                #相遇了
                res = head
                while res != slow:
                    slow = slow.next
                    res = res.next
                return res
        return None

