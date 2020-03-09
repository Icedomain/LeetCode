#
# @lc app=leetcode.cn id=303 lang=python3
#
# [303] 区域和检索 - 数组不可变
#
class NumArray:

    def __init__(self, nums: List[int]):
        self.list = [0] *(len(nums)+1)
        for i in range(len(nums)):
            self.list[i+1] = self.list[i] + nums[i]

    def sumRange(self, i: int, j: int) -> int:
        return self.list[j+1] - self.list[i]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)

