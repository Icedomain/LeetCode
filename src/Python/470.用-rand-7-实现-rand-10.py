#
# @lc app=leetcode.cn id=470 lang=python3
#
# [470] 用 Rand7() 实现 Rand10()
#
class Solution:
    def rand10(self):
        num = (rand7() - 1) * 7 + rand7()
        while num > 40:
            num = (rand7() - 1) * 7 + rand7()
        return 1 + (num - 1) % 10
