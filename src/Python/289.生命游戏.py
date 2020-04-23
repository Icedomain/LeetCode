#
# @lc app=leetcode.cn id=289 lang=python3
#
# [289] 生命游戏
#
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        '''
        # 卷积的思想
        import numpy as np
        r,c = len(board),len(board[0])
        #下面两行做zero padding
        board_exp=np.zeros((r+2,c+2))
        board_exp[1:-1,1:-1]=np.array(board)
        #设置卷积核
        kernel=np.array([[1,1,1],[1,0,1],[1,1,1]])
        #开始卷积
        for i in range(1,r+1):
            for j in range(1,c+1):
                #统计细胞周围8个位置的状态
                temp_sum=np.sum(kernel*board_exp[i-1:i+2,j-1:j+2])
                #按照题目规则进行判断
                if board_exp[i,j]==1:
                    if temp_sum<2 or temp_sum>3:
                        board[i-1][j-1]=0
                else:
                    if temp_sum==3:
                        board[i-1][j-1]=1
        return
        '''

        """
        方法二:两次遍历
        第一次遍历时也是分两种情况：
            若活细胞变成了死细胞,由1->-1
            若死细胞变成了活细胞,由0->2
        第二次遍历则是将2(活)->1, -1(死)->0
        """
        row_len, col_len = len(board), len(board[0])
        for row in range(row_len):
            for col in range(col_len):
                lives = self.count(board,row, col,row_len ,col_len )
                if board[row][col] == 1:
                    if lives < 2 or lives > 3:
                        board[row][col] = -1
                else:
                    if lives == 3:
                        board[row][col] = 2
        # 第二次遍历,恢复更改的值
        for row in range(row_len):
            for col in range(col_len):
                if board[row][col] == 2:
                    board[row][col] = 1
                elif board[row][col] == -1:
                    board[row][col] = 0
        return 

    def count(self,board,row, col ,row_len ,col_len ):
        lives = 0
        start_row ,end_row = max(0, row - 1) ,min(row_len-1, row+1)
        start_col, end_col = max(0, col - 1), min(col_len-1, col+1)
        for r in range(start_row, end_row+1):
            for c in range(start_col, end_col+1):
                if board[r][c] in [-1, 1] and not (r == row and c == col):
                    lives += 1
        return lives
        
