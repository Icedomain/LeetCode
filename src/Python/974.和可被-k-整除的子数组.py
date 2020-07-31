#
# @lc app=leetcode.cn id=974 lang=python3
#
# [974] 和可被 K 整除的子数组
#
class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        sums = [0] # 0相当于可以整除
        tmp = 0
        for x in A:
            tmp += x
            tmp %= K
            sums.append(tmp)
        dic = {}
        for i in sums:
            dic[i] = dic.get(i,0)+1

        res = 0
        for _,val in dic.items():
            res += val*(val-1)//2
        return res
