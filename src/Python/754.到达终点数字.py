#
# @lc app=leetcode.cn id=754 lang=python3
#
# [754] 到达终点数字
#
class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        sums, k = 0, 0
        # 和比目标值还小 或者不同奇偶
        while sums < target or (sums - target) % 2 != 0:
            k += 1
            sums += k
        return k
