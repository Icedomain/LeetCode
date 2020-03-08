#
# @lc app=leetcode.cn id=67 lang=python3
#
# [67] 二进制求和
#
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if not a: 
            return b
        if not b: 
            return a
        # 最后都是1 前面的相加 再加1 补0
        if a[-1] == '1' and b[-1] == '1':
            return self.addBinary(self.addBinary(a[0:-1],b[0:-1]),'1')+'0'
        # 最后都是0 补0
        if a[-1] == '0' and b[-1] == '0':
            return self.addBinary(a[0:-1],b[0:-1])+'0'
        # 最后一个1 一个0 补1
        else:
            return self.addBinary(a[0:-1],b[0:-1])+'1'

