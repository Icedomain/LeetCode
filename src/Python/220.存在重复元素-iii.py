#
# @lc app=leetcode.cn id=220 lang=python3
#
# [220] 存在重复元素 III
#
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if t < 0 or k < 0:
            return False
        all_buckets = {}
        # 桶的大小设成t+1更加方便
        bucket_size = t + 1
        for i in range(len(nums)):
            # 放入哪个桶
            bucket_num = nums[i] // bucket_size 
            # 桶中已经有元素了
            if bucket_num in all_buckets:       
                return True
            # 把nums[i]放入桶中
            all_buckets[bucket_num] = nums[i]   
            # 检查前一个桶
            if (bucket_num - 1) in all_buckets and abs(all_buckets[bucket_num - 1] - nums[i]) <= t: 
                return True
            # 检查后一个桶
            if (bucket_num + 1) in all_buckets and abs(all_buckets[bucket_num + 1] - nums[i]) <= t: 
                return True
            
            # 如果不构成返回条件，那么当i >= k 的时候就要删除旧桶了，以维持桶中的元素索引跟下一个i+1索引只差不超过k
            if i >= k:
                all_buckets.pop(nums[i-k]//bucket_size)
                
        return False

