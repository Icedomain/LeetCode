#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
#
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        # 去除异常
        if not nums or len(nums) < 4:
            return res
        nums.sort()
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


