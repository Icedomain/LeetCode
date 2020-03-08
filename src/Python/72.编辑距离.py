#
# @lc app=leetcode.cn id=72 lang=python3
#
# [72] 编辑距离
#
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l1, l2 = len(word1)+1, len(word2)+1
        dp = [[0 for _ in range(l2)] for _ in range(l1)]
        # 行列处理 对应从空到一个字符串 或 一个字符串到空
        for i in range(l1):
            dp[i][0] = i
        for j in range(l2):
            dp[0][j] = j
        for i in range(1, l1):
            for j in range(1, l2):
                if word1[i-1]==word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    # 三个分别对应于加、减、替换
                    dp[i][j] = min(dp[i-1][j],
                                   dp[i][j-1], 
                                   dp[i-1][j-1]
                                   )+1
        return dp[-1][-1]

