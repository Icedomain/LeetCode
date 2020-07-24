#
# @lc app=leetcode.cn id=43 lang=python3
#
# [43] 字符串相乘
#
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        #把num1,num2翻转方便计算
        num1 = num1[::-1]; num2 = num2[::-1]
        #每一位互相乘的结果用一维数组去储存
        arr = [0 for i in range(len(num1)+len(num2))]
        #填充这个一维数组
        for i in range(len(num1)):
            for j in range(len(num2)):
                arr[i+j] += int(num1[i]) * int(num2[j])

        res = []
        # arr是反的
        for i in range(len(arr)):
            # digit表示这一位的数字 carry表示加给下一位的量
            digit , carry = arr[i] % 10 , arr[i] // 10
            if i < len(arr) - 1 :
                #下一位加上
                arr[i+1] += carry
            res.append(str(digit))
        #去除首位为0的情况
        while res[-1] == '0' and len(res) > 1:
            res.pop()
        return ''.join(res[::-1])

