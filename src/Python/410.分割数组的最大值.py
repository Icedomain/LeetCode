#
# @lc app=leetcode.cn id=410 lang=python3
#
# [410] 分割数组的最大值
#
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        # 最大值最小的范围(单个最大,整体和)
        left = max(nums) 
        right = sum(nums)

        while left < right:
            mid = (right + left) // 2
            count = self.count(nums,mid)
            if count > m:
                # 次数太多说明 mid值太小
                left = mid + 1
            else:
                right = mid
        return left

    def count(self,nums,mid):
        tmpsum = 0
        count = 1
        for num in nums:
            tmpsum += num
            if tmpsum > mid:
                tmpsum = num
                count += 1
        return count
