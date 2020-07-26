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
        dummy = ListNode(-float('inf'))
        dummy.next = head

        cur = head
        while cur and cur.next:
            # 顺序的
            if cur.val < cur.next.val:
                cur = cur.next
                continue
            val = cur.next.val
            # 找到p(小于的最后一个节点)
            p = dummy
            while p.next.val < val:
                p = p.next
            # 右边的节点插入到左边去
            # p p.next cur cur.next cur.next.next 换成
            # p cur.next p.next cur cur.next.next
            next_step = cur.next
            cur.next = cur.next.next
            next_step.next = p.next
            p.next = next_step
        return dummy.next

