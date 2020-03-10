#
# @lc app=leetcode.cn id=551 lang=python3
#
# [551] 学生出勤记录 I
#
class Solution:
    def checkRecord(self, s: str) -> bool:
        count = 0
        for i in range(len(s)): 
            if s[i] =='A':
                # 大于1个A
                count += 1
                if count > 1:
                    return False        
            elif s[i] == 'L' and 0 < i < len(s)-1 \
                and s[i-1] == 'L' == s[i+1]: 
                return False
        return True

