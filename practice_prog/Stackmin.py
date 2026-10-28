class MinStack:
    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, val):
        self.stack.append(val)

        if not self.minstack:
            self.minstack.append(val)
        else:
            self.minstack.append(min(val,self.minstack[-1]))

    def pop(self):
        self.stack.pop()
        self.minstack.pop()

    def top(self):
        return self.stack[-1]

    def minstacktop(self):
        return self.minstack[-1]

s = MinStack()
s.push(8)
s.push(20)
s.push(30)
s.push(5)
s.pop()

print(s.top(),s.minstacktop())

