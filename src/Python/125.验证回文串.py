#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] 验证回文串
#
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 检测字符串是否由字母和数字组成
        alnum = [t.lower() for t in s if t.isalnum()]
        leng = len(alnum)
        mid  = leng//2
        if leng < 2 :
            return True
        for i in range(mid):
            if alnum[i] != alnum[leng - i -1]:
                return False
        return True

