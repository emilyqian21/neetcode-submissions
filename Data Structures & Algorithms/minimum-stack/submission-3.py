class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = [] #用来记录历史最小值。 为什么用stack 而不是用一个单一的值？因为如果我pop掉了最小值，这个单一的值就不会更新

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minstack:
            self.minstack.append(min(val,self.minstack[-1]))
        else:
            self.minstack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        # how to get minimum in stack with O(1)? 
        return self.minstack[-1]