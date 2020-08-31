#
# @lc app=leetcode.cn id=977 lang=python3
#
# [977] 有序数组的平方
#

class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        n = len(A)
        # i: 从中间数第一个负的
        # j: 从中间数第一个正的
        j = 0
        while j < n and A[j] < 0:
            j += 1
        i = j - 1

        res = []
        while 0 <= i and j < n:
            # 哪个小先加哪个
            if A[i]**2 < A[j]**2:
                res.append(A[i]**2)
                i -= 1
            else:
                res.append(A[j]**2)
                j += 1
        # 剩下的解决完
        while i >= 0:
            res.append(A[i]**2)
            i -= 1
        while j < n:
            res.append(A[j]**2)
            j += 1
        return res

