#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长上升子序列
#
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        '''
        dp = [1] * len(nums)
        for i in range(1,len(nums)):
            for j in range(i):
                # 如果要求非严格递增,将此行 '<' 改为 '<=' 即可
                if(nums[j] < nums[i]):
                    dp[i] = max(dp[i] , dp[j] + 1 )
        return max(dp)
        '''

        up_list = []
        for i in range(len(nums)):
            # 二分查找
            left, right = 0, len(up_list)-1
            while left <= right:          
                mid = (left+right)//2
                if up_list[mid] < nums[i]:
                    left = mid+1
                else:
                    right = mid-1
            # 若 left 等于数组长度，则需要添加新值；否则，在 left 位置的值覆盖为新值
            if left == len(up_list):
                up_list.append(nums[i])
            else:
                up_list[left] = nums[i]
        return len(up_list)

