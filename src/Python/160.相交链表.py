#
# @lc app=leetcode.cn id=160 lang=python3
#
# [160] 相交链表
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        p1, p2 = headA, headB                       
        # 初始化两个运动结点p1和p2
        while p1 != p2:                             
            # 只要两个结点还未相遇
            p1 = p1.next if p1 else headB  
            # 如果p1走到了链表A的末尾，则换到链表B上
            p2 = p2.next if p2 else headA  
            # 如果p2走到了链表B的末尾，则换到链表A上
        return p1                                   

