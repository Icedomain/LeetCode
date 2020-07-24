#
# @lc app=leetcode.cn id=54 lang=python3
#
# [54] 螺旋矩阵
#
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []

        '''
        # 常规方法太烦了
        res = []
        xbegin = ybegin = 0
        xend = len(matrix[0]) - 1
        yend = len(matrix) - 1
        while True :
            # 横
            for j in range(xbegin,xend+1):
                res.append(matrix[ybegin][j])
            ybegin += 1
            if ybegin > yend :
                break
            # 竖
            for j in range(ybegin,yend+1):
                res.append(matrix[j][xend])
            xend -= 1
            if xbegin > xend:
                break
            # 横
            for j in range(xend,xbegin-1,-1):
                res.append(matrix[yend][j])
            yend -= 1
            if ybegin > yend :
                break
            # 竖
            for j in range(yend,ybegin-1,-1):
                res.append(matrix[j][xbegin])
            xbegin += 1
            if xbegin > xend:
                break
        return res
        '''
        
        m,n = len(matrix),len(matrix[0])
        x = y = di = 0
        dx = [0,1,0,-1]
        dy = [1,0,-1,0]
        res = []
        visited = set()

        for _ in range(m*n):
            res.append(matrix[x][y])
            visited.add((x,y))
            # 下一个点
            nx,ny = x+dx[di],y+dy[di]
            if 0<=nx<m and 0<=ny<n and (nx,ny) not in visited:
                x,y = nx,ny   
            else:
                # 如果不满足条件，换一个方向进行遍历
                di = (di+1)%4  
                nx,ny = x+dx[di],y+dy[di]
                x,y = nx,ny
        return res

