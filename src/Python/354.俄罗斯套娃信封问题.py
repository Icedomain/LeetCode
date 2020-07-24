#
# @lc app=leetcode.cn id=354 lang=python3
#
# [354] 俄罗斯套娃信封问题
#
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if not envelopes:
            return 0
        '''
        # 超时
        envelopes.sort(key=lambda x:x[0])
        dp = [1] * len(envelopes)
        for i in range(len(envelopes)):
            for j in range(i):
                if envelopes[i][0] > envelopes[j][0] and envelopes[i][1] > envelopes[j][1]:
                    dp[i] = max(dp[i],dp[j]+1)
        return max(dp)
        '''

        from bisect import bisect_left
        # 在L中查找x,x存在时返回x左侧的位置,x不存在返回应该插入的位置
        # 按w升序,h降序排列
        envelopes.sort(key=lambda x:(x[0], -x[1]))
        up_list = []
        for e in envelopes:
            index = bisect_left(up_list, e[1])
            if index == len(up_list):
                up_list.append(e[1])
            else:
                up_list[index] = e[1]
        return len(up_list)

