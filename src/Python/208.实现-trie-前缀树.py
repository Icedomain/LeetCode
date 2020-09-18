#
# @lc app=leetcode.cn id=208 lang=python3
#
# [208] 实现 Trie (前缀树)
# 
from collections import defaultdict
class TrieNode(object):
    def __init__(self):
        self.nodes = defaultdict(TrieNode)
        self.isword = False

class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root
        for char in word:
            cur = cur.nodes[char]
        cur.isword = True

    def search(self, word):
        cur = self.root
        for char in word:
            # cur.nodes 是 字典 
            # 判断 char 在不在字典里 
            if char not in cur.nodes:
                return False
            cur = cur.nodes[char]
        return cur.isword

    def startsWith(self, prefix):
        cur = self.root
        for char in prefix:
            if char not in cur.nodes:
                return False
            cur = cur.nodes[char]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

