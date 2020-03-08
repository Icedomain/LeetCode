#
# @lc app=leetcode.cn id=135 lang=python3
#
# [135] 分发糖果
#
class Solution:
    def candy(self, ratings: List[int]) -> int:
        if not ratings:
            return 0
        leng = len(ratings)
        res = [1 for _ in range(leng)]
        for i in range(1,leng):
            # 右边大
            if ratings[i] > ratings[i-1]:
                res[i] = res[i-1] + 1
        for i in range(leng-1 , 0 , -1 ):
            # 左边大
            if ratings[i-1] > ratings[i]:
                res[i-1] = max(res[i]+1 ,res[i-1])
        return sum(res)

