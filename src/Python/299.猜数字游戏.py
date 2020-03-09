#
# @lc app=leetcode.cn id=299 lang=python3
#
# [299] 猜数字游戏
#
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        a = b = 0
        dic = {}
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                a += 1
            dic[secret[i]] = dic.get(secret[i],0) + 1
        for i in range(len(guess)):
            if guess[i] in dic and dic[guess[i]] > 0 :
                b += 1
                dic[guess[i]] -= 1 
        b -= a
        return f"{a}A{b}B"
