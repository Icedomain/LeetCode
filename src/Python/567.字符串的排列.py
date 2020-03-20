#
# @lc app=leetcode.cn id=567 lang=python3
#
# [567] 字符串的排列
#
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        dic = [0] * 26
        for i in range(len(s1)):
            dic[ord(s1[i]) - ord('a')] -= 1
            dic[ord(s2[i]) - ord('a')] += 1
        
        for i in range(len(s2)-len(s1)):
            if sum(list(map(abs,dic))) == 0 :
                return True
            else:
                # 滑动窗往右滑动
                dic[ord(s2[i+len(s1)]) - ord('a')] += 1
                dic[ord(s2[i]) - ord('a')] -= 1    
        return sum(list(map(abs,dic))) == 0

