#
# @lc app=leetcode.cn id=921 lang=python3
#
# [921] 使括号有效的最少添加
#
class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        stack = []
        for ch in S:
            if stack and stack[-1] == '(' and ch == ')':
                stack.pop()
            else:
                stack.append(ch)
        return len(stack)


    def minAddToMakeValid2(self, S: str) -> int:
        # left表示需要补齐的左括号，right表示需要补齐的右括号
        left = right = 0 
        for ch in S:
            # 是 ) 就抵消一个
            if ch == '(':
                right += 1
            else:
                right -= 1
            
            if right < 0: # 此时说明右括号超过了左括号数
                left += 1
                right += 1 # 重置right，左括号已补齐
        
        return left + right

