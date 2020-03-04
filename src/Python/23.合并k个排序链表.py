#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并K个排序链表
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        return self.mergeK(lists, 0, len(lists) - 1)

    def mergeK(self, lists, low, high):
        if low == high:
            return lists[low]
        elif low + 1 == high:
            return self.mergeTwolists(lists[low], lists[high])
        mid = (low + high) // 2
        return self.mergeTwolists(self.mergeK(lists, low, mid), self.mergeK(lists, mid + 1, high))

    def mergeTwolists(self, l1, l2):
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        head = curr = ListNode(-1)
        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        curr.next = l1 or l2
        return head.next

