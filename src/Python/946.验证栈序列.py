#
# @lc app=leetcode.cn id=946 lang=python3
#
# [946] 验证栈序列
#
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        for num in pushed:
            stack.append(num)
            # 循环判断与出栈
            while stack and popped and stack[-1] == popped[0]: 
                stack.pop()
                popped.pop(0)
        return not stack

