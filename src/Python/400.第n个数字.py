#
# @lc app=leetcode.cn id=400 lang=python3
#
# [400] 第N个数字
#
class Solution:
    def findNthDigit(self, n: int) -> int:
        # 位数 起点 这个区间的数量
        # eg 各位 1开始 共9个
        digit, start, count = 1, 1, 9
        while n > count: # 1.
            n -= count
            start *= 10
            digit += 1
            count = 9 * start * digit
        # 该位置对应的数字是多少 eg 310
        num = start + (n - 1) // digit # 2.
        # 返回数字对应的位数
        return int(str(num)[(n - 1) % digit]) # 3.
