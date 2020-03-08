#
# @lc app=leetcode.cn id=143 lang=python3
#
# [143] 重排链表
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        if head is None or head.next is None:
            return head
        p1 ,p2 = head , head
        while p2 and p2.next :
            p1 = p1.next
            p2 = p2.next.next
        # head2 是后面半部分
        head2 = p1.next
        p1.next = None
        # head head2 对应前后两部分

        cur = head2
        rever = None
        # 反转
        while cur:
            temp = cur.next
            cur.next = rever
            rever = cur
            cur = temp
        
        # head rever 两个合并
        p1 = head
        while rever:
            # 两个链的下一个
            temp = p1.next
            temp2 = rever.next
            # 链接好
            p1.next = rever
            rever.next = temp
            # 下一个循环
            p1 = temp 
            rever = temp2
        return head

