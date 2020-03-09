#
# @lc app=leetcode.cn id=225 lang=python3
#
# [225] 用队列实现栈
#
class MyStack:
    def __init__(self):
        self.list = []
        
    def push(self, x: int) -> None:
        # 尾部压入
        self.list.append(x)

    def pop(self) -> int:
        # 尾部弹出
        if len(self.list) == 0:
            return
        else:
            temp = self.list[-1]
            del self.list[-1]
            return temp

    def top(self) -> int:
        if len(self.list) == 0:
            return
        else:
            return self.list[-1]

    def empty(self) -> bool:
        return len(self.list) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

