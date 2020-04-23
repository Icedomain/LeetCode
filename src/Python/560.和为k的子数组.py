#
# @lc app=leetcode.cn id=560 lang=python3
#
# [560] 和为K的子数组
#
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        '''  
        # 超时      
        same_length = 0
        for start in range(len(nums)):
            sums = 0
            for end in range(start, len(nums)):
                sums += nums[end]
                if sums == k:
                    same_length += 1
        return same_length
        '''

        count = 0
        sums = 0
        dic = {0:1}
        
        for num in nums:
            sums += num
            count += dic.get(sums-k,0)
            dic[sums] = dic.get(sums,0) + 1
        
        return count

