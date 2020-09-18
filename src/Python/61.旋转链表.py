#
# @lc app=leetcode.cn id=61 lang=python3
#
# [61] 旋转链表
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head is None or k == 0:
            return head
        
        cur = head
        length = 1
        while cur.next:
            cur = cur.next
            length += 1
        
        # 左部分多少个
        k = length - k%length

        # 连成一个环
        cur.next = head

        for _ in range(k):
            cur = cur.next
        
        # 断开
        head = cur.next
        cur.next = None
        return head

