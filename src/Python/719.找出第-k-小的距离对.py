#
# @lc app=leetcode.cn id=719 lang=python3
#
# [719] 找出第 k 小的距离对
#

class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        # 二分搜索 + 双指针
        nums.sort()
        low, high = 0, nums[-1] - nums[0]
        while low < high:
            mid = (low + high) // 2
            # 淘汰策略
            # 对于mid而言
            # 若小于mid的距离差总数 >= k，则距离差应落在 [low, mid] 之间
            # 若大于mid的距离差总数 < k，则距离差应落在 [mid+1, high] 之间
            count = self.cnt(nums, mid)
            if count >= k:
                high = mid
            else:
                low = mid + 1
        return low

    def cnt(self, nums: list, target: int) -> int:
        # 由于数组已有序，所以我们只需要统计差值在target内的数量即可
        # 大于target的我们可以直接跳过，以此来减少计算次数
        # 依然使用动态窗口机制，我们每次计算至差值 <= target
        # 则窗口向右滑动时，两侧元素差值 > target，我们可以直接将左侧元素剔除
        left, count = 0, 0
        for right in range(1, len(nums)):
            # 每次将right与 [left, right] 中的每个元素进行比较
            # 由于数组有序，我们只需要将left移动至第一个满足 right-left <= tartget
            # 的位置即可，中间的元素即为满足条件的元素
            # 若无元素满足条件，则left追上right
            while nums[right] - nums[left] > target:
                left += 1
            count += right - left
        return count


