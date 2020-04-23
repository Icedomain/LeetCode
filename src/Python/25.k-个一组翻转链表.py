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
        dummy = ListNode(0)
        dummy.next = head
        start = dummy
        end = start.next
        
        count = 0
        while end:
            count += 1
            if count % k == 0:
                # 返回为新一轮的头
                start = self.reverse(start, end.next)
                end = start.next
            else:
                end = end.next
        return dummy.next
    
    def reverse(self, start, end):
        # 输入一个是前驱,一个后驱
        prev, curr = start, start.next
        first = curr
        while curr != end:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        start.next = prev
        first.next = end
        return first

