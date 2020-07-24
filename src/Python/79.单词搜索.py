#
# @lc app=leetcode.cn id=79 lang=python3
#
# [79] 单词搜索
#
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m , n = len(board) , len(board[0])
        visited = [[False for i in range(n)] for i in range(m)]
        # 遍历寻找开头
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and self.dfs(board,word,visited,i,j,0):
                    return True
        return False

    def dfs(self,board,word,visited,i,j,start):
        # 终止条件
        if start == len(word):
            return True
        # 溢出 剪枝 or 已经访问过了
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or visited[i][j] or board[i][j] != word[start]:
            return False
        
        if board[i][j] == word[start]:
            visited[i][j] = True
            ret =   self.dfs(board,word,visited,i+1,j,start+1) or \
                    self.dfs(board,word,visited,i-1,j,start+1) or \
                    self.dfs(board,word,visited,i,j+1,start+1) or \
                    self.dfs(board,word,visited,i,j-1,start+1)
            visited[i][j] = False

            return ret

