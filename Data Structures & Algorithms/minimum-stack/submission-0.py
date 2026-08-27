class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        

    def pop(self) -> None:
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        minV = self.stack[-1]

        for i in range(len(self.stack)-2, -1, -1):
            if self.stack[i] < minV:
                minV = self.stack[i]
        
        return minV





        
