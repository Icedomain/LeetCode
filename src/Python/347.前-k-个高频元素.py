#
# @lc app=leetcode.cn id=347 lang=python3
#
# [347] 前 K 个高频元素
#
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    # def topKFrequent(self, nums, k):
        dic = dict(Counter(nums))
        arr = sorted(dic.items() ,key = lambda x : - x[1])
        return [x[0] for x in arr[:k] ]

    def topKFrequent2(self, nums: List[int], k: int) -> List[int]:
        # 字典统计出现频率
        dic = dict(Counter(nums))
        arr = list(dic.items())
        lenth = len(dic.keys())
        # 构造规模为k的minheap
        if k <= lenth:
            k_minheap = arr[:k]
            # 从后往前建堆
            for i in range(k // 2 - 1, -1, -1): 
                self.heapify(k_minheap, k, i)
            # 对于k:, 大于堆顶则入堆，维护规模为k的minheap
            for i in range(k, lenth):
                if arr[i][1] > k_minheap[0][1]:
                    k_minheap[0] = arr[i]
                    self.heapify(k_minheap, k, 0)
        # 如需按顺序输出，对规模为k的堆进行排序
        # 从尾部起，依次与顶点交换再构造minheap，最小值被置于尾部
        for i in range(k - 1, 0, -1):
            k_minheap[i], k_minheap[0] = k_minheap[0], k_minheap[i]
            k -= 1 # 交换后，维护的堆规模-1
            self.heapify(k_minheap, k, 0)
        return [item[0] for item in k_minheap]

    def heapify(self, arr, n, i):
        smallest = i
        l = 2 * i + 1
        r = 2 * i + 2
        if l < n and arr[l][1] < arr[i][1]:
            smallest = l
        if r < n and arr[r][1] < arr[smallest][1]:
            smallest = r
        if smallest != i:
            arr[i], arr[smallest] = arr[smallest], arr[i]
            self.heapify(arr, n, smallest)


