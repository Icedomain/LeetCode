#
# @lc app=leetcode.cn id=65 lang=python3
#
# [65] 有效数字
#
class Solution:
    def isNumber(self, s: str) -> bool:
        states = [
            # 0. start with 'blank'
            { ' ': 0, 's': 1, 'd': 2, '.': 4 }, 
            # 1. 'sign' before 'e'
            { 'd': 2, '.': 4 } ,             
            # 2. 'digit' before 'dot'   
            { 'd': 2, '.': 3, 'e': 5, ' ': 8 }, 
            # 3. 'digit' after 'dot'
            { 'd': 3, 'e': 5, ' ': 8 },     
            # 4. 'digit' after 'dot' (‘blank’ before 'dot')    
            { 'd': 3 },                         
            # 5. 'e'
            { 's': 6, 'd': 7 },       
            # 6. 'sign' after 'e'          
            { 'd': 7 },         
            # 7. 'digit' after 'e'               
            { 'd': 7, ' ': 8 },          
            # 8. end with 'blank'       
            { ' ': 8 }                          
        ]
        p = 0
        for c in s:
            if '0' <= c <= '9': t = 'd' # digit
            elif c in "+-": t = 's'     # sign
            elif c in ".eE ": t = c     # dot, e, blank
            else: t = '?'               # unknown
            if t not in states[p]: 
                return False
            p = states[p][t]
        return p in (2, 3, 7, 8)
