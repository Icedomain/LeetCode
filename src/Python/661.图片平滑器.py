#
# @lc app=leetcode.cn id=661 lang=python3
#
# [661] 图片平滑器
#
class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
    #def imageSmoother(self, M):
        r = len(M)
        c = len(M[0])
        res = []
        
        for i in range(r):
            tmp = []
            for j in range(c):
                value,count=M[i][j],1
                if i-1>=0:
                    value += M[i-1][j]
                    count += 1
                    if j-1>=0:
                        value += M[i-1][j-1]
                        count += 1
                    if j+1<c:
                        value += M[i-1][j+1]
                        count += 1
                if i+1<r:
                    value += M[i+1][j]
                    count += 1
                    if j-1>=0:
                        value += M[i+1][j-1]
                        count += 1
                    if j+1<c:
                        value += M[i+1][j+1]
                        count += 1
                if j-1>=0:
                    value += M[i][j-1]
                    count += 1
                if j+1<c:
                    value += M[i][j+1]
                    count += 1
                tmp.append(int(value/count))
            res.append(tmp)
        return res

