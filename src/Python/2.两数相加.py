#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        jingwei = 0
        # 两个空指针 n后面要被覆盖的
        head = n = ListNode(0)
        while l1 or l2 or jingwei:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            # 除数、余数
            val = (v1+v2+jingwei) % 10
            jingwei = (v1+v2+jingwei) // 10
            n.next = ListNode(val)
            # 指向下一个
            n = n.next
        return head.next # 记得把第一个0去掉


