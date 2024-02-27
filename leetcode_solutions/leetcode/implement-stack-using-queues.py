class MyStack:

    def __init__(self):
        self.first= deque()
        
        

    def push(self, x: int) -> None:
        self.first.append(x)
        

    def pop(self) -> int:
        val=self.first.pop()
        return val
        

    def top(self) -> int:
        return self.first[-1]
        

    def empty(self) -> bool:
        return False if self.first else True
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()