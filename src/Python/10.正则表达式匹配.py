#
# @lc app=leetcode.cn id=10 lang=python3
#
# [10] 正则表达式匹配
#
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        '''
        # 递归写法
        # s已被匹配且p已耗完
        if not s and not p:
            return True
        # p已耗完但s未被完全匹配
        if len(s) > 0 and len(p) == 0:
            return False

        # 如果模式第二个字符是*
        if len(p) > 1 and p[1] == '*':
            if len(s) > 0 and (s[0] == p[0] or p[0] == '.'): # ax a* or ax .*
                # 如果第一个字符匹配，三种可能1、p后移两位；2、字符串移1位
                return self.isMatch(s, p[2:]) or self.isMatch(s[1:], p)
            else:
                # 如果第一个字符不匹配，p往后移2位，相当于忽略x*
                return self.isMatch(s, p[2:])
        # 如果模式第二个字符不是*
        if len(s) > 0 and (s[0] == p[0] or p[0] == '.'):
            return self.isMatch(s[1:], p[1:])
        else:
            return False
        '''
        # 动态规划
        # 初始化dp表，初始化表的第一列和第一行
        # p对应列 s对应行
        dp = [[False for j in range(len(p) + 1)] for i in range(len(s) + 1)]
        dp[0][0] = True  # s 和 p 都为空时
        # 若 s 为空时
        # 处理第一行
        # p 与 dp 有一位的错位(多了一个空导致的)
        for j in range(1, len(p) + 1):
            # dp[0][j]= (p[j-1]=="*")and(j>=2)and(dp[0][j-2])           
            # 等同于下列语句
            if p[j - 1] == '*':
                if j >= 2:
                    dp[0][j] = dp[0][j - 2]
        # 第一列就第一个是 True,下面都是 False
        # 不用处理 pass

        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                #  j-1才为正常字符串中的索引
                #  p当前位置为"*"时
                # 代表空串--dp[i][j-2]
                # 一个或者多个前一个字符--( dp[i-1][j] and (p[j-2]==s[i-1] or p[j-2]=='.')
                if p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 2] or (
                                dp[i - 1][j] and (p[j - 2] == s[i - 1] or p[j - 2] == '.')
                                )
                #  p当前位置为"."时或者与s相同时，传递dp[i-1][j-1]的真值
                else:
                    dp[i][j] = (p[j - 1] == '.' or p[j - 1] == s[i - 1]) and dp[i - 1][j - 1]
        return dp[-1][-1]



