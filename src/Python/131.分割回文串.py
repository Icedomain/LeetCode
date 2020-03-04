#
# @lc app=leetcode.cn id=131 lang=python3
#
# [131] 分割回文串
#
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        self.recurPartition(s,result, [],  0)
        return result

    def recurPartition(self,s, result, curr, start):
        if start == len(s):
            result.append(list(curr))
            return 
        for i in range(start, len(s)):
            if self.isPalindrome(s, start, i):
                curr.append(s[start:i+1])
                self.recurPartition(s,result,curr ,i + 1)
                curr.pop()
    # 判断回文
    def isPalindrome(self, s, begin, end):
        while begin < end :
            if s[begin] != s[end]:
                return False
            begin += 1
            end -= 1
        return True
