#
# @lc app=leetcode.cn id=661 lang=python3
#
# [661] 图片平滑器
#
class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        row, col = len(M), len(M[0])
        res = [[0] * col for _ in range(row)]

        for r in range(row):
            for c in range(col):
                # 计算个数和值
                count = 0
                for nr in range(r-1, r+2 ):
                    for nc in range(c-1, c+2 ):
                        if 0 <= nr < row and 0 <= nc < col:
                            res[r][c] += M[nr][nc]
                            count += 1
                res[r][c] //= count
        return res

