#
# @lc app=leetcode.cn id=38 lang=python3
#
# [38] 外观数列
#
class Solution:
    def countAndSay(self, n: int) -> str:
        s = '1'
        for _ in range(n-1):
            s = self.count(s)
        return s
    
    def count(self ,s):
        m = list(s)
        # 加一个后面不会溢出(随便加一个就行)
        # 数字和字符肯定是不一样的
        m.append(5)
        res = ()
        i,j = 0,0
        while i < len(m)-1 and j < len(m) :
            j += 1
            if m[j] != m[i]:
                res += (str(j-i) , m[i] )
                i = j
        # 用空元素链接res
        return ''.join(res)

