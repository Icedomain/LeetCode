#
# @lc app=leetcode.cn id=147 lang=python3
#
# [147] 对链表进行插入排序
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        p = dummy = ListNode(-1000)
        dummy.next = head
        cur = head
        while cur and cur.next:
            val = cur.next.val
            # 顺序的
            if cur.val < val:
                cur = cur.next
                continue
            # 找到p(小于的最后一个节点)
            if p.next.val > val:
                p = dummy
            while p.next.val < val:
                p = p.next
            # 交换节点
            next_step = cur.next
            cur.next = next_step.next
            next_step.next = p.next
            p.next = next_step
        return dummy.next

