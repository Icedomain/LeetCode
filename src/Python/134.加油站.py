#
# @lc app=leetcode.cn id=134 lang=python3
#
# [134] 加油站
#
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        sumGas = sumCost = 0
        start = 0
        diff = 0
        for i in range(len(gas)):
            sumGas += gas[i]
            sumCost += cost[i]
            diff += gas[i] - cost[i]
            if diff < 0:
                start = i + 1 ## 下一个开始
                diff = 0
        return start if sumGas - sumCost >= 0 else -1 

