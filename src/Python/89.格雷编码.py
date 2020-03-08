#
# @lc app=leetcode.cn id=89 lang=python3
#
# [89] 格雷编码
#
class Solution:
    def grayCode(self, n: int) -> List[int]:
        res = [0]
        for i in range(n):
            for j in range(len(res)-1,-1,-1):
                res.append(res[j] + (1 << i))
        return res
