#
# @lc app=leetcode.cn id=140 lang=python3
#
# [140] 单词拆分 II
#
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n = len(s)
        dp = [False for _ in range(n+1)]
        dp[0] = True
        # prev true 表示s[j,i)是一个合法单词,从j处切开
        prev = [[False for _ in range(n)] for _ in range(n+1) ]
        
        for i in range(n+1):
            for j in range(i-1,-1,-1):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    prev[i][j] = True

        res = []
        self.dfs(s,prev,n,[],res)
        return res

    def dfs(self,s,prev,cur,path,res):
        if cur == 0:
            # 终止条件
            temp = " ".join(path)
            res.append(temp)
            return

        for i in range(cur-1,-1,-1):
            if prev[cur][i]:
                self.dfs(s,prev,i,[s[i:cur]] + path,res)


