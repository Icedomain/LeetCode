#
# @lc app=leetcode.cn id=71 lang=python3
#
# [71] 简化路径
#
class Solution:
    def simplifyPath(self, path: str) -> str:
        res = []
        for child in path.split('/'):
            if child in ('' , '.'):
                pass
            elif child == '..':
                if res:
                    res.pop()
            else:
                res.append(child)
        return '/' + '/'.join(res)

