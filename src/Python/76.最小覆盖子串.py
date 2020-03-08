#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s is None or len(s) < len(t):
            return ""
        res = ""
        left = 0
        right = 0
        min_len = len(s)
        count = 0

        m = {}
        # 统计t中字符数目
        for i in t:
            m[i] = m.get(i,0) + 1
        
        while right < len(s):
            if s[right] in m:
                # 先找到一个区间能包含t,但长度不一定是最短的
                m[s[right]] -= 1
                if m[s[right]] >= 0:
                    count += 1
                # 找到了一个区间
                while (count == len(t)):
                    # 选择更短的子串
                    if (right - left + 1 < min_len):
                        min_len = right-left+1
                        res = s[left:right+1]
                    
                    if s[left] in m:
                        m[s[left]] += 1
                        if m[s[left]] > 0:
                            count -= 1
                    left += 1
            right += 1
            
        return res

