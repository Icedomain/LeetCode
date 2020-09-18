#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#
from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s is None or len(s) < len(t):
            return ""
        # 需求字典
        need = defaultdict(int)
        for ch in t:
            need[ch] += 1
        
        # 避免每次都统计need情况
        needCnt = len(t)

        #记录起始位置 并记录起终点
        i = 0 
        res = (0, float('inf'))  

        for j,c in enumerate(s):
            # c 在need(t) 里面 , 不在t里的不会大于0
            if need[c] > 0:
                needCnt -= 1
            need[c] -= 1
            # 收缩左边界直到无法再去掉元素
            # 注意，处理的是i
            if needCnt == 0:
                while i < j :
                    if need[s[i]] == 0: #表示再去掉就不行了(need>0)
                        break
                    else:
                        # 右移
                        need[s[i]] += 1
                        i += 1
                # 子串更新
                if j-i < res[1] - res[0]:
                    res = (i,j)
                # i右移(注意这步是在 needCnt == 0里面进行的 )
                # 字典维护 需求加一 区间右移
                need[s[i]] += 1
                needCnt += 1
                i += 1
        return "" if res[1]>len(s) else s[res[0]: res[1]+1]

