#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N皇后
#
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        # C[i]表示第i行皇后在哪一列
        C = [-1 for _ in range(n)]
        self.dfs(C,result,0)
        return result
    
    def dfs(self,C,res,row):
        N = len(C)
        # 终止条件
        if N == row :
            path = [["." for _ in range(N)] for _ in range(N)]
            for i in range(N):
                # (i,C[i])位置对应皇后
                path[i][C[i]] = "Q"
            path = ["".join(r) for r in path]
            # if path not in res:
            # 不用排除
            res.append(path)
            return
        # 对该行每一列都进行尝试,可以的话下一行
        for j in range(N):
            if j not in C and self.isOK(C,row,j):         
                C[row] = j
                self.dfs(C,res,row+1)
                C[row] = -1

    # 对该行之前的都进行判断,返回合理与否
    def isOK(self,C,row,col):
        for i in range(row):
            # 同一列
            # 同一对角线
            if C[i] == col or abs(i-row) == abs(C[i]-col):
                return False
        return True

