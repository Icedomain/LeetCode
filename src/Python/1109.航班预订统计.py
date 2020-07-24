#
# @lc app=leetcode.cn id=1109 lang=python3
#
# [1109] 航班预订统计
#
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        # 每个航班人数 计数器
        count = [0] * n
        for book in bookings:
            # 航班1-n转化为0-1
            # 上车加
            count[book[0]-1] += book[2]
            if book[1] < n:
                # 下车减
                count[book[1]] -= book[2]
        # 从前到尾的累和
        for i in range(1,n):
            count[i] += count[i-1]
        return count

