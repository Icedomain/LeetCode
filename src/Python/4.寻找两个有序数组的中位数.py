#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个有序数组的中位数
#
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        leng = len(nums1)+len(nums2)
        # 奇数
        if leng %2 :
            return self.findk(nums1,nums2,leng//2)
        else:
            return (self.findk(nums1,nums2,leng//2-1)+self.findk(nums1,nums2,leng//2))/2.0
    # 找k大的数
    def findk(self,nums1,nums2,k):
        if not nums1:
            return nums2[k]
        if not nums2:
            return nums1[k]
        l1 , l2 = len(nums1)//2,len(nums2)//2
        val1 ,val2 = nums1[l1],nums2[l2]

        if l1+l2<k:
            # 个数太少
            # 往右找
            if val1 > val2:
                return self.findk(nums1, nums2[l2 + 1:], k - l2 - 1)
            else:
                return self.findk(nums1[l1 + 1:],nums2, k - l1 - 1)
        else: 
            # 左边个数多了
            # 往左找
            if val1 > val2:
                return self.findk(nums1[:l1],nums2, k)
            else:
                return self.findk(nums1, nums2[:l2], k)

