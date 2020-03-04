#
# @lc app=leetcode.cn id=150 lang=python3
#
# [150] 逆波兰表达式求值
#
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        for t in tokens:
            if t not in ['+','-','*','/']:
                nums.append(int(t))
            else:
                r = nums.pop()
                l = nums.pop()
                if t == '+':
                    temp = l+r
                elif t == '-':
                    temp = l-r
                elif t == '*':
                    temp = l*r
                elif t == '/':
                    if l*r < 0 and l%r != 0:
                        temp = l//r + 1
                    else:
                        temp = l//r             
                nums.append(temp)
        return nums.pop()
        

