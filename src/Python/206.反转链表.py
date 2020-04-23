#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        '''
        if head is None or head.next is None:
            return head
        curr = head # 他来往后走
        prev = None  # 新的反转的
        while curr:
            # 下一步先保存下来
            nextcurr = curr.next
            # 反转的接上去
            curr.next = prev
            prev  = curr
            # 下一步
            curr = nextcurr
        return prev
        '''
        # 递归方法
        if not head:
            return None
        if not head.next:
            return head
        headNode = self.reverseList(head.next)
        # head headNode 顺序(环)
        head.next.next = head
        # head headNode head(断开)
        head.next = None
        return headNode
