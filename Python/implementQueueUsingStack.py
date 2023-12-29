class MyQueue:
    queueStack = []
    temp = []

    def __init__(self):
        self.queueStack = []
        self.temp = []

    def push(self, x: int) -> None:
        while self.queueStack:
            self.temp.append(self.queueStack.pop())
        self.queueStack.append(x)

        while self.temp:
            self.queueStack.append(self.temp.pop())


    def pop(self) -> int:
        return self.queueStack.pop()

    def peek(self) -> int:
        return self.queueStack[len(self.queueStack)-1]

    def empty(self) -> bool:
        return len(self.queueStack) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()