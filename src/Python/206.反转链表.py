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
        cur = head # 他来往后走
        prev = None  # 新的反转的
        while cur:
            # 下一步先保存下来
            nextcur = cur.next
            # 反转的接上去
            cur.next = prev
            prev  = cur
            # 下一步
            cur = nextcur
        return prev
        '''
        # 递归方法
        if not head or not head.next:
            return head
        headNode = self.reverseList(head.next)
        # head headNode 顺序(环)
        head.next.next = head
        # head headNode head(断开)
        head.next = None
        return headNode
