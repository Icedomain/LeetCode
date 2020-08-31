#
# @lc app=leetcode.cn id=395 lang=python3
#
# [395] 至少有K个重复字符的最长子串
#

import collections
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if not s :
            return 0
        cnt = collections.Counter(s)
        st = 0
        maxst = 0
        for i, c in enumerate(s):
            if cnt[c] < k :
                maxst = max(maxst, 
                self.longestSubstring(s[st:i], k))
                st = i + 1
        if st == 0:
            return len(s)
        else:
            return max(maxst, 
            self.longestSubstring(s[st:], k)
            )
