#
# @lc app=leetcode.cn id=306 lang=python3
#
# [306] 累加数
#
class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        # 题意解读：确认前两个数字，后面即被确认
        # 思路：遍历前两个数字，优化是遍历不超过num_str的一半即可
        # 限制:开头不可为0--->但有'000'的情况，len(num)至少为3
        # 0可以作为一个数字，但不能有以0开头的数字
        len_num = len(num)
        if len_num < 3:
            return False

        for i in range(len_num//2 + 1):
            num1 = num[:i+1]
            # 若num1是以0开头的数字，return Fasle
            if num1[0] =='0' and i >= 1 :
                return False
            
            for j in range(i+1, len_num//2+i+1):
                num2 = num[i+1:j+1]
                # 若num2以0开头，break
                if num2[0] =='0' and j >= i + 2 :
                    break
                num3 = num[j+1:]
                if self.isValid(num1, num2, num3) and num3:
                    return True
        return False

    def isValid(self, num1, num2, num3):
        # 已确定前两个数字，判断是否合法
        while num3:
            sum_num = str(int(num1) + int(num2))
            if num3.startswith(sum_num):
                num1 = num2
                num2 = sum_num
                num3 = num3[len(sum_num):]
            else:
                return False
        return True
