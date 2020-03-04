#
# @lc app=leetcode.cn id=665 lang=python3
#
# [665] 非递减数列
#
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        count = 0
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                count +=1
                #变相去掉nums[i]
                if i <1 or nums[i-1] <= nums[i+1]:
                    nums[i] = nums[i+1]
                else:
                    # 变相去掉nums[i+1]
                    nums[i+1]=nums[i]
        return count <= 1


