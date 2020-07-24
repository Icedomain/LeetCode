#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
#
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # 去除异常
        if not nums or len(nums) < 4:
            return []
        nums.sort()
    
        
        res = []
        # 第一个数遍历
        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # 第二个数遍历
            for j in range(i + 1, len(nums) - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                # 双指针
                L, R = j + 1, len(nums) - 1
                while L < R:
                    if nums[i] + nums[j] + nums[L] + nums[R] == target:
                        res.append([nums[i], nums[j], nums[L], nums[R]])
                        while L < R and nums[L] == nums[L + 1]:
                            L += 1
                        while L < R and nums[R] == nums[R - 1]:
                            R -= 1
                        L += 1
                        R -= 1
                    elif nums[i] + nums[j] + nums[L] + nums[R] < target:
                        L += 1
                    else:
                        R -= 1
        return res

        '''
        # 方法二 递归
        res = self.nSumTarget(nums ,4 , 0 , target)
        return res
        '''

    def nSumTarget(self ,nums , n , start , target ):
        sz = len(nums)
        res = []
        if n < 2 :
            return []
        elif n == 2:
            l ,r = start , sz - 1
            while l < r :
                val = nums[l] + nums[r]
                if val < target:
                    l += 1
                elif val > target :
                    r -= 1
                else:
                    res.append([nums[l] , nums[r]])
                    while (l<r and nums[l] == nums[l+1]) : l += 1
                    while (l<r and nums[r] == nums[r-1]) : r -= 1
                    l += 1
                    r -= 1
        else :
            i = start
            while i < sz :
                sub = self.nSumTarget(nums,n-1,i+1,target-nums[i])
                for arr in sub:
                    arr.append(nums[i])
                    res.append(arr)
                while i < sz - 1 and nums[i]==nums[i+1] :
                    i += 1
                i += 1
        return res

