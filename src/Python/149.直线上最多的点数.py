#
# @lc app=leetcode.cn id=149 lang=python3
#
# [149] 直线上最多的点数
#
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if points is None :
            return 0
        res = 0
        # 两重循环
        # 双重字典
        for i in range(len(points)):
            line_map = {}
            same = max_point_num = 0
            for j in range(i + 1, len(points)):
                dx, dy = points[j][0] - points[i][0], points[j][1] - points[i][1]
                # 同一个点
                if dx == 0 and dy == 0:
                    same += 1
                    continue
                # 去除最大公约数部分
                gcd = self.generateGCD(dx, dy)
                if gcd != 0:
                    dx //= gcd
                    dy //= gcd
                
                if dx in line_map:
                    if dy in line_map[dx]:
                        line_map[dx][dy] += 1
                    else:
                        line_map[dx][dy] = 1
                else:
                    line_map[dx] = {}
                    line_map[dx][dy] = 1
                max_point_num = max(max_point_num, line_map[dx][dy])
            res = max(res, max_point_num + same + 1)
        return res

    # 辗转相除法求最大公约数
    def generateGCD(self, x, y):
        if y == 0:
            return x
        else:
            return self.generateGCD(y, x % y)

