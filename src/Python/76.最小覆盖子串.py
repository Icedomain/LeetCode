#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#
import collections
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s is None or len(s) < len(t):
            return ""
        need = collections.defaultdict(int)
        # 需求字典
        for c in t:
            need[c] += 1
        # 避免每次都统计need情况
        needCnt = len(t)
        #记录起始位置
        i = 0 
        # 用两个元素，方便之后记录起终点
        res = (0, float('inf'))  

        # 增加右边界使滑窗包含t
        for j,c in enumerate(s):
            # 不在t里的不会大于0
            if need[c] > 0:
                needCnt -= 1
            need[c] -= 1
            # 收缩左边界直到无法再去掉元素
            # 注意，处理的是i
            if needCnt == 0:
                while True:
                    c = s[i]
                    if need[c] == 0: #表示再去掉就不行了(need>0)
                        break
                    else:
                        need[c] += 1
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

