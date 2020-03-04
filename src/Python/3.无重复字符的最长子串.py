#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 记录表 256个字符
        charmap = [-1 for _ in range(256)]

        start = maxlen = 0
        # 遍历 滑动窗 [start,j] j往右边移动 若遇到重复的 start又移一位
        for j in range(len(s)):
            # 如果这个字符出现过了，又移动 最左边那个踢出滑动窗
            if charmap[ord(s[j])] >= start:
                start = charmap[ord(s[j])] + 1
            # 如果这个字符在滑动窗中没出现过，位置给它(出现过也要给它)
            charmap[ord(s[j])] = j
            maxlen = max(maxlen , j-start +1)
        return maxlen

