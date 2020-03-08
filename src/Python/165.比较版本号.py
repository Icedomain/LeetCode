#
# @lc app=leetcode.cn id=165 lang=python3
#
# [165] 比较版本号
#
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        vs1 = version1.split('.')
        vs2 = version2.split('.')
        l1 , l2 = len(vs1) , len(vs2)
        if (l1 > l2):
            vs2 += [0] *(l1-l2) 
        elif l1 < l2:
            vs1 += [0] *(l2-l1) 
        n = max(l1,l2)
        for i in range(n):
            if int(vs1[i]) > int(vs2[i]):
                return 1
            elif int(vs1[i]) < int(vs2[i]):
                return -1
        return 0

