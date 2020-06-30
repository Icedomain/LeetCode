#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#
class Solution:
    #def maxSubArray(self, nums: List[int]) -> int:
    def maxSubArray(self, nums):
        '''
        temp = maxsum = nums[0]
        for num in nums[1:]:
            # num 要么单独一个子列,要么归入别的子列
            temp = max(num,temp+num)
            maxsum = max(temp,maxsum)
        return maxsum
        '''
        maxNum = nums[0]
        for i in range(1,len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
            maxNum = max(maxNum,nums[i])
        return maxNum

    def maxSubArray2(self, nums):
        maxNum = nums[0]
        start = end = 0
        finalStart = finalEnd = 0
        for i in range(1,len(nums)):
            # 滑动窗右移
            # 判断上一个是不是正数
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
                end = i
            # 重新开滑动窗
            else:
                start = end = i
            # 要更新的
            if nums[i] > maxNum:
                finalStart = start
                finalEnd = end
                maxNum = nums[i]
        return [finalStart, finalEnd]

a = Solution().maxSubArray2([-2,1,-3,4,-1,2,1,-5,4])
print(a)