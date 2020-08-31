#
# @lc app=leetcode.cn id=232 lang=python3
#
# [232] 用栈实现队列
#
class MyQueue:
    def __init__(self):
        self.st1 = []
        self.st2 = []

    def push(self, x: int) -> None:
        # 尾部加入
        self.st1.append(x)

    def pop(self) -> int:
        while len(self.st1) > 1:
            self.st2.append(self.st1.pop())
        res = self.st1.pop()
        while self.st2:
            self.st1.append(self.st2.pop())
        return res

    def peek(self) -> int:
        # pop 和 peek 差一个队首的 append
        while len(self.st1) > 1:
            self.st2.append(self.st1.pop())
        res = self.st1.pop()
        self.st2.append(res)
        while self.st2:
            self.st1.append(self.st2.pop())
        return res

    def empty(self) -> bool:
        return len(self.st1) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

