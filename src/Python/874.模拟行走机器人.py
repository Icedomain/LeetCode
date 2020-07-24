#
# @lc app=leetcode.cn id=874 lang=python3
#
# [874] 模拟行走机器人
#
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        # 北 东 南 西 四个方向 顺时针描述
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        di, x, y = 0, 0, 0
        distance = 0
        # 时间溢出
        dic = set()
        for obs in obstacles:
            dic.add(tuple(obs))

        for com in commands:
            if com == -2:
                di = (di + 3)%4
            elif com == -1:
                di = (di + 1)%4
            else:
                # 走多步
                for _ in range(com):
                    next_x = x + dx[di]
                    next_y = y + dy[di]
                    if (next_x, next_y) in dic:
                        break
                    x, y = next_x, next_y
                    distance = max(distance, x*x + y*y)
        return distance

