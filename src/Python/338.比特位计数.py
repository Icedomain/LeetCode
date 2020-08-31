#
# @lc app=leetcode.cn id=338 lang=python3
#
# [338] 比特位计数
#

class Solution:
    def countBits(self, num: int) -> List[int]:
        res = [0] *(num+1)
        for i in range(1,num+1):
            # 奇数
            if i % 2 :
                res[i] = res[i-1] + 1
            # 偶数
            else:
                res[i] = res[i//2]

        return res
