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
        rev = None
        slow = fast = head
        # fast 到尾部
        # slow 到中部
        # rev 前半部分的反向
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next ,slow = slow, rev , slow.next
        # 奇
        if fast:
            slow = slow.next
        # 一个向左,一个向右
        while rev :
            if rev.val != slow.val:
                return False
            slow = slow.next
            rev = rev.next
        return True

