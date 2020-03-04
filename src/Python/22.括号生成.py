#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        if n > 0 :
            self.dfs(n,'',res,0,0)
        return res

    def dfs(self,n,path,res, left, right):
        # 终止条件
        if len(path) == 2 * n:
            res.append(path)
            return
        # 左括号(够了没
        if left < n:
            self.dfs(n,path+'(',res, left+1, right)
        # 右括号补成和左括号一样多
        if left > right:
            self.dfs(n,path+')',res, left, right+1)

