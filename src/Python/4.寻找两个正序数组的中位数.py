#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个有序数组的中位数
#
class Solution:
    def findMedianSortedArrays2(self, nums1: List[int], nums2: List[int]) -> float:
        k1 = ( len(nums1) + len(nums2) + 1 ) // 2
        k2 = ( len(nums1) + len(nums2) + 2 ) // 2
        return (self.findk(nums1,nums2,k1) + \
                self.findk(nums1,nums2,k2))/2.0

    # 找第k小的数
    # O(log min(m,n)))
    def findk(self,nums1,nums2,k):
        # 长 短
        if len(nums1) < len(nums2):
            return self.findk(nums2,nums1,k)
        if not nums2:
            return nums1[k-1]
        if k == 1:
            return min(nums1[0],nums2[0])
        idx = min(k//2,len(nums2))

        if nums1[idx-1] > nums2[idx-1] :
            return self.findk(nums1,nums2[idx:],k-idx)
        else:
            return self.findk(nums1[idx:],nums2,k-idx)

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        ls = len(nums1) + len(nums2)
        # 奇数
        if ls % 2 :
            return self.kth(nums1,nums2,ls//2)
        else:
            k1 = ( len(nums1) + len(nums2) + 1 ) // 2 - 1
            k2 = ( len(nums1) + len(nums2) + 2 ) // 2 - 1
            return (self.kth(nums1,nums2,k1) + \
                    self.kth(nums1,nums2,k2))/2.0

    # O(log(m+n)) 
    def kth(self,nums1,nums2,k):
        if not nums1:
            return nums2[k]
        if not nums2:
            return nums1[k]
        l1 , l2 = len(nums1)//2,len(nums2)//2
        val1 ,val2 = nums1[l1],nums2[l2]

        if l1+l2 < k:
            # 个数太少
            # 往右找
            if val1 > val2:
                return self.kth(nums1,nums2[l2+1:], k-l2-1)
            else:
                return self.kth(nums1[l1+1:],nums2, k-l1-1)
        else: 
            # 左边个数多了
            # 往左找
            if val1 > val2:
                return self.kth(nums1[:l1],nums2, k)
            else:
                return self.kth(nums1,nums2[:l2], k)

