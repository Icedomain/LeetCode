#
# @lc app=leetcode.cn id=109 lang=python3
#
# [109] 有序链表转换二叉搜索树
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        '''
        if not head :
            return None
        if not head.next:
            return TreeNode(head.val)

        slow = head
        fast = head.next.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        head2 = slow.next
        slow.next = None
        root = TreeNode(head2.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(head2.next)
        return root 
        '''

        if not head :
            return None
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        return self.sortedArrayToBST(nums)

    def sortedArrayToBST(self, nums):
        if not nums :
            return None
        mid = len(nums)//2

        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])

        return root

