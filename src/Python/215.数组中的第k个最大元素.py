#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        '''
        nums.sort()
        return nums[-k]
        '''
        return self.qSelect(nums, 0, len(nums) - 1, k)

    def qSelect(self, nums, start, end, k):
        '''
        if start > end:
            return float('inf')
        '''
        # 找一个参照值
        pivot = nums[end]
        left = start
        for i in range(start, end):
            # 比参照大的都移到左边去
            if nums[i] >= pivot:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
        # 参照值也拉倒左边去
        nums[left], nums[end] = nums[end], nums[left]
        # 左边的个数够没(从0开始到k-1,共k个)
        if left == k-1:
            return nums[left]
        # 还不够
        elif left < k-1:
            return self.qSelect(nums, left + 1, end, k)
        # 太多了
        else:
            return self.qSelect(nums, start, left - 1, k)

