#
# @lc app=leetcode.cn id=6 lang=python3
#
# [6] Z 字形变换
#
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        # z前半个(|/)个数两行减2
        p = 2 * (numRows - 1)

        result = [""] * numRows
        for i in range(len(s)):
            floor = i % p # 一个形状轮回的位置
            if floor >= p//2: # 在/上
                floor = p - floor
            result[floor] += s[i]
        return "".join(result)
