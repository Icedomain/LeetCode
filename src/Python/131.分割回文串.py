#
# @lc app=leetcode.cn id=131 lang=python3
#
# [131] 分割回文串
#
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        self.dfs(s,res, [],  0)
        return res

    def dfs(self,s, res, path, start):
        if start == len(s):
            res.append(path)
            return 
        # start -> i 是回文的 
        for i in range(start, len(s)):
            if self.isPalindrome(s, start, i):
                self.dfs(s,res,path +[s[start:i+1]],i + 1)
    # 判断回文
    def isPalindrome(self, s, begin, end):
        while begin < end :
            if s[begin] != s[end]:
                return False
            begin += 1
            end -= 1
        return True
