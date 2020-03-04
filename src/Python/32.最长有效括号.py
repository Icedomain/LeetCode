#
# @lc app=leetcode.cn id=32 lang=python3
#
# [32] 最长有效括号
#
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        '''
        # 栈法
        res = []
        stack = []
        for i in range(len(s)):
            if(stack and s[i]==")"):
                res.append(stack.pop())
                res.append(i)
            if(s[i]=="("):
                stack.append(i)
        
        res.sort()
        max_len = 0
        i=0
        while i < len(res)-1:
            tmp = i
            # 最长连续值
            while( i < len(res)-1 and res[i+1]-res[i] == 1):
                i += 1
            max_len = max(max_len,i-tmp+1)
            i += 1
        return max_len
        '''

        # 动态规划
        if not s:
            return 0
        dp = [0] * len(s)
        for i in range(1,len(s)):
            if s[i]==")":
                # ()对
                if s[i-1]=="(":
                    dp[i] = dp[i-2] + 2
                # 连着两个))
                if s[i-1]==")" and i-1-dp[i-1]>=0 and s[i-1-dp[i-1]]=="(":
                    dp[i] = dp[i-dp[i-1]-2] + dp[i-1] + 2
        return max(dp)

