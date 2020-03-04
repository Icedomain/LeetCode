#
# @lc app=leetcode.cn id=92 lang=python3
#
# [92] 反转链表 II
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        for i in range(m-1):
            prev = prev.next
        
        temp = None
        cur = prev.next
        for i in range(n-m+1):
            next = cur.next
            # reverse
            cur.next = temp
            temp = cur
            # 下一个
            cur = next

        # 最后面一段
        prev.next.next = cur
        '''
        wi = temp
        while wi.next is not None:
            wi = wi.next
        wi.next = cur
        '''
        # 中间一段
        prev.next = temp

        return dummy.next

