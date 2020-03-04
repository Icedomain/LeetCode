#
# @lc app=leetcode.cn id=264 lang=python3
#
# [264] 丑数 II
#
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly = [1]
        i2,i3,i5 = 0,0,0
        idx = 1
        while idx < n :
            newugly = min([ugly[i2]*2 , ugly[i3]*3 ,ugly[i5]*5])
            ugly.append(newugly)

            while ugly[i2]*2<= newugly:
                i2 += 1
            while ugly[i3]*3<= newugly:
                i3 += 1
            while ugly[i5]*5<= newugly:
                i5 += 1
            idx += 1            
        return ugly[-1]
        

