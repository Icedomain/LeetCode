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
            p1 = headB if p1 is None else p1.next   
            # 如果p1走到了链表A的末尾，则换到链表B上
            p2 = headA if p2 is None else p2.next   
            # 如果p2走到了链表B的末尾，则换到链表A上

        return p1                                   
        # 当p1和p2都换到对方的链表上，再次相遇后第一个结点即为首个公共结点，否则为None

