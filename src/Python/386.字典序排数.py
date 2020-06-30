#
# @lc app=leetcode.cn id=386 lang=python3
#
# [386] 字典序排数
#
# Python的富比较方法包括__lt__、__gt__分别表示:小于、大于，对应的操作运算符为:“<”、“>”
class LargerNumKey(int):
    def __lt__(x, y):
        return str(x) < str(y)

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        '''
        return list(sorted(range(1, n+1), key = LargerNumKey))
        '''
        res = []
        for i in range(1, 10):
            self.dfs(i,n,res)
        return res
        

    def dfs(self,i,n,res):
        if i <= n:
            res.append(i)
            for d in range(10):
                self.dfs(10 * i + d,n,res)
