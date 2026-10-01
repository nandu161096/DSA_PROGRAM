class MinStack:
    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, val):
        self.stack.append(val)

        if not self.minstack:
            self.minstack.append(val)
        else:
            self.minstack.append(min(val, self.minstack[-1]))

    def pop(self,val):
        self.stack.pop(val)
        self.minstack.pop(val)

    def top(self):
        return self.stack[-1]

    def minstacktop(self):
        return self.minstack[-1]


s = MinStack()
s.push(5)
s.push(2)
s.push(8)
s.push(1)

print(s.top(),s.minstacktop())

