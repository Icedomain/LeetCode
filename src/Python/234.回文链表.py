#
# @lc app=leetcode.cn id=234 lang=python3
#
# [234] 回文链表
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None:
            return True
        # slow 到中部   fast 到尾部
        # prev 前半部分的反向
        slow = fast = head
        prev = None
        while fast and fast.next:
            fast = fast.next.next
            prev, prev.next, slow = slow, prev, slow.next
        # 奇
        if fast:
            slow = slow.next
        # 一个向左,一个向右
        while prev :
            if prev.val != slow.val:
                return False
            slow = slow.next
            prev = prev.next
        return True

