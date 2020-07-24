#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第N个节点
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head:
            return None
        dummy = ListNode(-1)
        dummy.next = head
        slow = fast = dummy
        # 先走n步
        for _ in range(n):
            fast = fast.next

        # slow 少走n步
        while fast.next :
            fast = fast.next
            slow = slow.next
        # 删除
        slow.next = slow.next.next
        return dummy.next

