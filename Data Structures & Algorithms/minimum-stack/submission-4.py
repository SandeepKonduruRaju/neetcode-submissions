class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, val: int) -> None:
        
        self.stack.append(val)
        if self.minstack:
            if val <= self.minstack[-1]:
                self.minstack.append(val)       
        else:
            self.minstack.append(val)
        #print("self.stack",self.stack,"minstack",self.minstack,"val",val)

    def pop(self) -> None:
        poppedEle = self.stack.pop()
        if self.minstack[-1] == poppedEle:
            self.minstack.pop()
        #print("[POP CALL self.stack",self.stack,"minstack",self.minstack,"poppedEle",poppedEle)
        return poppedEle

    def top(self) -> int:
        #print("[TOP CALL self.stack",self.stack,"minstack",self.minstack)
        return self.stack[-1]

    def getMin(self) -> int:
        if self.minstack:
            return self.minstack[-1]
        