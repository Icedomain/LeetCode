#
# @lc app=leetcode.cn id=605 lang=python3
#
# [605] 种花问题
#
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        for i in range(len(flowerbed)):
            curr = flowerbed[i]
            if i >= 1:
                curr += flowerbed[i - 1]
            if i < len(flowerbed)-1:
                curr += flowerbed[i + 1]
            if curr == 0:
                count += 1
                flowerbed[i] = 1

        return count>=n


