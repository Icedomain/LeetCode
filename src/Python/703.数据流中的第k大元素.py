#
# @lc app=leetcode.cn id=703 lang=python3
#
# [703] 数据流中的第K大元素
#

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.k = k
        # 小顶堆
        heapq.heapify(self.nums)
        # 只留 k 个
        while len(self.nums) > self.k :
            heapq.heappop(self.nums)        

    def add(self, val: int) -> int:
        heapq.heappush(self.nums,val)
        while len(self.nums) > self.k :
            heapq.heappop(self.nums)
        return self.nums[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
