#
# @lc app=leetcode.cn id=204 lang=python3
#
# [204] 计数质数
#
class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        res = [0,0]+ [1]*(n-2)
        for i in range(2,n):
            # 这些没改过
            if res[i] == 1:
                for j in range(2,(n-1)//i+1):
                    res[i*j] = 0
        return sum(res)

