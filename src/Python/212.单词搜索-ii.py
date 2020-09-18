#
# @lc app=leetcode.cn id=212 lang=python3
#
# [212] 单词搜索 II
#
from collections import defaultdict
class TrieNode():
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isWord = False
    
class Trie():
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for w in word:
            node = node.children[w]
        node.isWord = True
    
    def search(self, word):
        node = self.root
        for w in word:
            node = node.children.get(w)
            if not node:
                return False
        return node.isWord

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = []
        # 建树
        trie = Trie()
        for w in words:
            trie.insert(w)
        
        node = trie.root
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, node, i, j, "", res)
        return res
    
    def dfs(self, board, node, i, j, path, res):
        if node.isWord:
            res.append(path)
            # 防止重复
            node.isWord = False
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return 
        
        cur = board[i][j]
        node = node.children.get(cur)
        if node:
            board[i][j] = "#"
            self.dfs(board, node, i+1, j, path+cur, res)
            self.dfs(board, node, i-1, j, path+cur, res)
            self.dfs(board, node, i, j-1, path+cur, res)
            self.dfs(board, node, i, j+1, path+cur, res)
            board[i][j] = cur

