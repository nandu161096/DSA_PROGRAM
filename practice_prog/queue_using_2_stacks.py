class QueueusingTwoStack:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enqueue(self, val):
        self.s1.append(val)

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return

        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())

        return self.s2.pop()

    def front(self):
        if self.is_empty():
            print("Queue is empty")
            return
        
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())

        return self.s2[-1]

    def is_empty(self):
        return len(self.s1) == 0 and len(self.s2) == 0


s = QueueusingTwoStack()
s.enqueue(10)
s.enqueue(20)
s.enqueue(30)

print(s.dequeue())
