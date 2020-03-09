#
# @lc app=leetcode.cn id=313 lang=python3
#
# [313] 超级丑数
#
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        ugly = [1]
        ls = len(primes)
        ix = [0]*ls
        idx = 1
        while idx < n :
            newugly = min([ugly[ix[i]]*primes[i] for i in range(ls)])
            ugly.append(newugly)
            for i in range(ls):
                while ugly[ix[i]]*primes[i]<= newugly:
                    ix[i] += 1
            idx += 1            
        return ugly[-1]

