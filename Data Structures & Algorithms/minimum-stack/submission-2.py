class MinStack:

    def __init__(self):
        self.stack=[]
        self.min_stack=[]

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.min_stack)>0:
            if self.min_stack[-1]<=val:
                self.min_stack.append(self.min_stack[-1])
            else:
                self.min_stack.append(val)
        else:
            self.min_stack.append(val)
        

    def pop(self) -> None:
        self.min_stack.pop()
        return self.stack.pop()

    def top(self) -> int:
        if len(self.stack)>0:
            return self.stack[-1]
        else:
            return -1
        

    def getMin(self) -> int:
        # print(self.stack,self.min_stack)
        return self.min_stack[-1]

        
