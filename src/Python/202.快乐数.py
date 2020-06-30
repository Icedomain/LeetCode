#
# @lc app=leetcode.cn id=202 lang=python3
#
# [202] 快乐数
#
class Solution:
    def isHappy(self, n: int) -> bool:
        mem = set()
        while n != 1:
            # 求和
            n = sum([int(i) ** 2 for i in str(n)])
            if n in mem:
                # 陷入死循环了
                return False
            else:
                mem.add(n)
        return True


