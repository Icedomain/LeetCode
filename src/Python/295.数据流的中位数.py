#
# @lc app=leetcode.cn id=295 lang=python3
#
# [295] 数据流的中位数
#
import heapq
class MedianFinder:
    def __init__(self):
        # 初始化大顶堆和小顶堆
        # 堆顶应该是最小的
        # min_heap是大数部分
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num: int) -> None:
        if len(self.max_heap) == len(self.min_heap):
            # 先加到大顶堆，再把大堆顶元素加到小顶堆
            heapq.heappush(self.min_heap, \
                -heapq.heappushpop(self.max_heap, -num))
        else:  
            # 先加到小顶堆，再把小堆顶元素加到大顶堆
            heapq.heappush(self.max_heap, \
                -heapq.heappushpop(self.min_heap, num))

    def findMedian(self) -> float:
        if len(self.min_heap) == len(self.max_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        else:
            return self.min_heap[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
