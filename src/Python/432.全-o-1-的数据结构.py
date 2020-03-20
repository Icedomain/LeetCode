#
# @lc app=leetcode.cn id=432 lang=python3
#
# [432] 全 O(1) 的数据结构
#        
class AllOne:
    def __init__(self):
        self.lookup = {}
        
    def inc(self, key: str) -> None:
        if key in self.lookup:
            self.lookup[key] += 1
        else:
            self.lookup[key] = 1
        
    def dec(self, key: str) -> None:
        if key in self.lookup:
            if self.lookup[key] == 1:
                self.lookup.pop(key)
            else:
                self.lookup[key] -= 1
    
    def getMaxKey(self) -> str:
        return max(self.lookup.items(), key=lambda x: x[1], default=[""])[0]
    
    def getMinKey(self) -> str:
        return min(self.lookup.items(), key=lambda x: x[1], default=[""])[0]

# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()

