#
# @lc app=leetcode.cn id=91 lang=python3
#
# [91] 解码方法
#
class Solution:
    def numDecodings(self, s: str) -> int:
        if s is None or s[0] == '0':
            return 0
        # dp[i] 表示s中前i个字符组成的子串的解码方法的个数，长度比输入数组长多多1，并将 dp[0] 初始化为1
        dp = [0] * (len(s)+1)
        dp[0] = dp[1] = 1
        for i in range(2,len(s)+1):
            if s[i - 1] >= '1' and s[i - 1] <= '9':
                dp[i] += dp[i - 1]
            if s[i-2]=='1' or (s[i-2] == '2' and s[i-1] <= '6'):
                dp[i] += dp[i - 2]
        return dp[-1]
