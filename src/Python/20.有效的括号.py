#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#
class Solution:
    def isValid(self, s: str) -> bool:
        # 判断是否是奇数或空字符
        if s=='':
            return True
        stack = []
        match = {')': '(', ']': '[', '}': '{'}
        for ch in s:
            if ch in match:
                if not (stack and stack.pop() == match[ch]):
                    return False
            else:
                stack.append(ch)
        return not stack

        '''
        if len(s) %2 != 0:
            return False
        count = 0
        leng = len(s)
        # 将其中的(){}[] 都换掉，然后判断是否有剩余
        while(count < leng/2 ):
            s = s.replace("{}","").replace("[]","").replace("()","")
            count+=1
        
        if len(s)>0:
            return False
        else:
            return True
        '''


