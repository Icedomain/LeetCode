#
# @lc app=leetcode.cn id=349 lang=python3
#
# [349] 两个数组的交集
#
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # return list(set(nums1) & set(nums2))
        '''
        res = []
        for i in nums1:
            if i not in res and i in nums2:
                res.append(i)
        
        return res
        '''
        nums1.sort()
        nums2.sort()
        if not nums1 or not nums2:
            return []
        if nums1[0] == nums2[0]:
            foo = self.intersection(nums1[1:],nums2[1:])
            if foo and foo[0] == nums1[0]:
                return foo
            else:
                return [nums1[0]]+foo
        elif nums1[0]<nums2[0]:
            return self.intersection(nums1[1:],nums2)
        else:
            return self.intersection(nums1,nums2[1:])


