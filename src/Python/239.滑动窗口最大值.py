#
# @lc app=leetcode.cn id=239 lang=python3
#
# [239] 滑动窗口最大值
#
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # deque 双向队列 左边代表的索引对应的值大
        deque = []
        res = []
        for i, n in enumerate(nums):
            # 左边的索引超出了滑动窗
            if deque and i - deque[0] == k:
                deque.pop(0)
            # 队列填充填充大数的原则 
            while deque and nums[deque[-1]] < n:
                deque.pop()
            deque.append(i)
            # 队列左端就是大的数
            if i >= k - 1:
                res.append(nums[deque[0]])
        return res

