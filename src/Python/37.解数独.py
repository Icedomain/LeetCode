#
# @lc app=leetcode.cn id=37 lang=python3
#
# [37] 解数独
#
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        self.dfs(board)

    def dfs(self,board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    for k in '123456789':
                        board[i][j] = k
                        # 修改一个值判断是不是合法的
                        # 如果这个递归可以返回true并且当前填入的数字也没毛病
                        # 则证明我们解完了数独
                        if self.isOK(board,i,j) and self.dfs(board):
                            return True
                        board[i][j] = '.'               
                    return False
        # 全部填完之后返回True
        return True

    def isOK(self,board,x,y):
        #列符合
        for i in range(9):
            if i != x and board[i][y] == board[x][y]:
                return False
        #检查行是否符合
        for j in range(9):
            if j != y and board[x][j] == board[x][y]:
                return False
        row_start = 3*(x // 3)
        col_start = 3*(y // 3)
        for i in range(row_start,row_start+3):
            for j in range(col_start,col_start+3):
                if (i!= x or j!= y) and board[i][j] == board[x][y]:
                    return False
        return True

