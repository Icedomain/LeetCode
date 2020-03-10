#
# @lc app=leetcode.cn id=661 lang=python3
#
# [661] 图片平滑器
#
class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        R, C = len(M), len(M[0])
        res = [[0] * C for _ in range(R)]

        for r in range(R):
            for c in range(C):
                count = 0
                for nr in (r-1, r, r+1):
                    for nc in (c-1, c, c+1):
                        if 0 <= nr < R and 0 <= nc < C:
                            res[r][c] += M[nr][nc]
                            count += 1
                res[r][c] //= count
        return res

