#
# @lc app=leetcode.cn id=128 lang=python3
#
# [128] 最长连续序列
#
class Solution:
    def longestConsecutive2(self, nums: List[int]) -> int:
        maxLen = 0
        while nums:
            n = nums.pop()
            # 往大处搜索
            i1 = n + 1
            while i1 in nums:
                nums.remove(i1)
                i1 += 1
            # 往小处搜索
            i2 = n - 1
            while i2 in nums:
                nums.remove(i2)
                i2 -= 1
            maxLen = max(maxLen, i1 - i2 - 1)
        return maxLen

    def longestConsecutive(self, nums: List[int]) -> int:
        dic = dict()
        maxLen = 0
        for num in nums:
            if num not in dic:
                left = dic.get(num - 1, 0)
                right = dic.get(num + 1, 0)
                
                curLen = 1 + left + right
                maxLen = max(maxLen , curLen )

                # 这里不是用于端点记录的
                # 而是标记num已经在hash中,所以可以是随便一个值
                dic[num] = 0
                dic[num - left] = curLen
                dic[num + right] = curLen
        return maxLen

