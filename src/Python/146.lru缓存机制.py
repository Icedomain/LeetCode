#
# @lc app=leetcode.cn id=146 lang=python3
#
# [146] LRU缓存机制
#
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        # 存放使用频率的key 大的放头
        self.queue = []        

    def get(self, key: int) -> int:
        if key in self.cache:
            # 更新一下操作的元素
            self.queue.remove(key)
            self.queue.insert(0,key)
            return self.cache[key]
        else:
            return -1        

    def put(self, key: int, value: int) -> None:
        if not key or not value:
            return None
        if key in self.cache: # 已经在了
            self.queue.remove(key)
        elif len(self.queue) == self.capacity: # 满了
            top = self.queue.pop()
            del self.cache[top]

        self.cache[key] = value
        self.queue.insert(0,key)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

