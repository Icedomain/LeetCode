#
# @lc app=leetcode.cn id=25 lang=python3
#
# [25] K 个一组翻转链表
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if head is None or k < 2:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        start , end = dummy, dummy.next
        
        count = 1
        while end:
            if count % k == 0:
                # 返回为新一轮的头
                start = self.reverse(start, end.next)
                end = start.next
            else:
                end = end.next
            count += 1
        return dummy.next
    
    def reverse(self, start, end):
        # 输入一个是前驱,一个后驱
        prev, cur = start.next, start.next
        first = cur
        while cur != end:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        start.next = prev
        first.next = end
        return first

