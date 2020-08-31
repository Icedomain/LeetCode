#
# @lc app=leetcode.cn id=225 lang=python3
#
# [225] 用队列实现栈
#
class MyStack:
    def __init__(self):
        self.que1 = []
        self.que2 = []
        
    def push(self, x: int) -> None:
        # 尾部压入
        self.que1.append(x)

    def pop(self) -> int:
        # 尾部弹出
        while len(self.que1) > 1:
            self.que2.append(self.que1.pop(0))
        res = self.que1.pop(0)
        while self.que2:
            self.que1.append(self.que2.pop(0))
        return res 

    def top(self) -> int:
        if len(self.que1) == 0:
            return
        else:
            return self.que1[-1]

    def empty(self) -> bool:
        return len(self.que1) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

