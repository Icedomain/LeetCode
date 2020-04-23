#
# @lc app=leetcode.cn id=93 lang=python3
#
# [93] 复原IP地址
#
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        self.dfs(s,[],res,0)
        return res
    
    def dfs(self,s,ip,res,start):
        # 终止条件
        if len(ip) == 4 and start == len(s):
            address = '.'.join(ip)
            res.append(address)
            return

        # 特殊场景下可以剪枝
        # 剩下的子串太长(剩下的ip位都超过了3位)或太短(剩下的ip位都小于1位了)
        if len(s) -start > 3*(4-len(ip)) or len(s) -start < (4-len(ip)):
            return

        # 最多三位(+0,+1,+2)
        for i in range(0,3):
            substr = s[start:start+i+1]
            # 允许单个0,但是不允许0开头的一串,比如025
            if i != 0 and substr[0] == '0':
                continue
            if int(substr) >= 0 and int(substr) <= 255:
                self.dfs(s,ip+[substr],res,start + i + 1)

