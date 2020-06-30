#
# @lc app=leetcode.cn id=130 lang=python3
#
# [130] 被围绕的区域
#
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if len(board) <= 2 or len(board[0])<=2:
            return 
        row , col = len(board) , len(board[0])
        # 对边界上的所有点分别进行深度遍历
        # 第一列和最后一列
        for i in range(row): 
            self.dfs(board,i,0,    row,col)
            self.dfs(board,i,col-1,row,col)
        # 第一行和最后一行
        for j in range(1,col-1):
            self.dfs(board,0,    j,row,col)
            self.dfs(board,row-1,j,row,col)
        
        for i in range(row):
            for j in range(col):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "T":
                    board[i][j] = "O"
        return 

    def dfs(self,board,i,j,row,col):
        if i < 0 or j < 0 or i >= row or j >= col or board[i][j] != "O":
            return 
        else:
            board[i][j] = "T"
            self.dfs(board,i-1,j,row,col)
            self.dfs(board,i,j-1,row,col)
            self.dfs(board,i+1,j,row,col)
            self.dfs(board,i,j+1,row,col)



