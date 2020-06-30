#
# @lc app=leetcode.cn id=885 lang=python3
#
# [885] 螺旋矩阵 III
#
class Solution:
    def spiralMatrixIII(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        A, d = [[r0,c0]], 0
        x , y = r0 ,c0
        while len(A) < R*C:
            # s代表方向 d 代表走的距离
            for s in (1,-1):
                d += 1
                for y in range(y+s,y+s*(d+1),s):
                    if 0<=x<R and 0<=y<C: 
                        A.append([x,y])
                for x in range(x+s,x+s*(d+1),s):
                    if 0<=x<R and 0<=y<C: 
                        A.append([x,y])
        return A

