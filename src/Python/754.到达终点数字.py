#
# @lc app=leetcode.cn id=754 lang=python3
#
# [754] 到达终点数字
#
class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        p, n = 0, 0
        # 和比目标值还小 或者不同奇偶
        while p < target or (p + target) % 2 != 0:
            n += 1
            p += n
        return n
