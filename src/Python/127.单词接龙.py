#
# @lc app=leetcode.cn id=127 lang=python3
#
# [127] 单词接龙
#
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # 防止时间超出
        wordset = set(wordList)
        # 初始化
        bfs = [(beginWord, 1)]
        while bfs:
            word,length = bfs.pop(0) # 左边弹出
            if word == endWord:
                return length
            for i in range(len(word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    # 不同位置都可以插入不同字母进行新单词重构
                    newWord = word[:i] + c + word[i + 1:]
                    if newWord in wordset and newWord != word:
                        wordset.remove(newWord)
                        bfs.append((newWord, length + 1))
        return 0


