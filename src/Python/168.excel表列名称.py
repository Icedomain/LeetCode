#
# @lc app=leetcode.cn id=168 lang=python3
#
# [168] Excel表列名称
#
class Solution:
    def convertToTitle(self, n: int) -> str:
        capitals = [chr(x) for x in range(ord('A'), ord('Z')+1)]
        result = []

        while n > 0:
            n -= 1
            result.append(capitals[n%26])
            n //= 26
        result.reverse()
        return ''.join(result)

