#
# @lc app=leetcode.cn id=52 lang=python3
#
# [52] N皇后 II
#
class Solution:
    def totalNQueens(self, n: int) -> int:
        self.res = 0
        # C[i]表示第i行皇后在哪一列
        C = [-1 for _ in range(n)]
        self.dfs(C,0)
        return self.res
    
    def dfs(self,C,row):
        N = len(C)
        # 终止条件
        if N == row :
            # 不用排除
            self.res += 1
        # 对该行每一列都进行尝试,可以的话下一行
        for j in range(N):
            if j not in C and self.isOK(C,row,j):           
                C[row] = j
                self.dfs(C,row+1)
                C[row] = -1

    # 对该行之前的都进行判断,返回合理与否
    def isOK(self,C,row,col):
        for i in range(row):
            # 同一列
            # 同一对角线
            if C[i] == col or abs(i-row) == abs(C[i]-col):
                return False
        return True        

