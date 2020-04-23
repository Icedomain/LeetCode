#
# @lc app=leetcode.cn id=179 lang=python3
#
# [179] 最大数
#
# Python的富比较方法包括__lt__、__gt__分别表示:小于、大于，对应的操作运算符为:“<”、“>”
class LargerNumKey(str):
    def __lt__(x, y):
        return x+y < y+x

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        '''
        if set(nums) == {0}: 
            return '0'
        str_nums = sorted([str(i) for i in nums], key=LargerNumKey,reverse = True)
        largest = "".join(str_nums)
        return largest
        '''
        
        if set(nums) == {0}: 
            return '0'
        for i in range(len(nums), 0, -1):
            tmp = 0
            for j in range(i):
                if not self.compare(nums[j], nums[tmp]):
                    tmp = j
            nums[tmp], nums[i-1] = nums[i-1], nums[tmp]
        return "".join(map(str, nums))
        
    def compare(self, n1, n2):
        return str(n1) + str(n2) > str(n2) + str(n1)
