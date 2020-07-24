#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#

class Solution:
    def findKthLargest2(self, nums: List[int], k: int) -> int:
        '''
        nums.sort()
        return nums[-k]
        '''
        return self.qSelect(nums, 0, len(nums) - 1, k)

    def qSelect(self, nums, start, end, k):
        # 找一个参照值
        pivot = nums[end]
        left , right = start ,end 
        for i in range(start, end):
            # 比参照大的都移到左边去
            if nums[i] >= pivot:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
        # 参照值也拉倒左边去
        nums[left], nums[end] = nums[end], nums[left]
        # 左边的个数够没(从0开始到k-1,共k个)
        if left == k-1:
            return nums[left]
        # 还不够
        elif left < k-1:
            return self.qSelect(nums, left + 1, end, k)
        # 太多了
        else:
            return self.qSelect(nums, start, left - 1, k)


    def findKthLargest(self, nums: List[int], k: int) -> int:
        if k == 0:
            return []
        self.randomized_selected(nums, 0, len(nums) - 1, k)
        return nums[k-1]
    
    def partition(self, nums, l, r):
        # 右边找参照
        pivot = nums[r]
        # 小的移到左边去
        i = l
        for j in range(l, r):
            if nums[j] >= pivot:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        nums[i], nums[r] = nums[r], nums[i]
        return i

    # 换到尾部
    def randomized_partition(self, nums, l, r):
        i = random.randint(l, r)
        nums[r], nums[i] = nums[i], nums[r]
        return self.partition(nums, l, r)

    def randomized_selected(self, arr, l, r, k):
        pos = self.randomized_partition(arr, l, r)
        # 左边有几个
        num = pos + 1
        # 左边数量太多了
        if k < num:
            self.randomized_selected(arr, l, pos - 1, k)
        # 左边数量太少了
        elif k > num:
            self.randomized_selected(arr, pos + 1, r, k)
        else:
            return
