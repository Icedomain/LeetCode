#
# @lc app=leetcode.cn id=126 lang=python3
#
# [126] 单词接龙 II
#
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        import collections
        wordset = set(wordList)
        
        level = {beginWord}
        # value 是前驱节点
        parents = collections.defaultdict(set)
        
        while level and endWord not in parents:
            next_level = collections.defaultdict(set)
            for word in level:
                # 不同位置都可以插入不同字母进行新单词重构
                for i in range(len(beginWord)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        newWord = word[:i] + c + word[i+1:]
                        if newWord in wordset and newWord not in parents:
                            next_level[newWord].add(word)
            level = next_level
            parents.update(next_level)

        res = [[endWord]]
        # parents相当于是逆向 
        # 对当前的res的每个段头添加前驱
        while res and res[0][0] != beginWord:
            # 确定是等长的
            res = [[p]+r for r in res for p in parents[r[0]]]
        return res


