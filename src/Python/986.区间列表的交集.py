#
# @lc app=leetcode.cn id=986 lang=python3
#
# [986] 区间列表的交集
#

class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        # 两个指针
        i , j = 0 , 0
        res = []
        while i < len(A) and j < len(B):
            a_start, a_end = A[i]
            b_start, b_end = B[j]
            # 交叉
            if a_start <= b_end and b_start <= a_end:
                res.append([max(a_start, b_start), min(a_end, b_end)])
            # 早结束的那个先离开
            if a_end <= b_end:
                i += 1
            else:
                j += 1
        return res
