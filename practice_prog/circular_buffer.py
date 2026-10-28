class CircularQueue:
    def __init__(self, size):
        self.size = size 
        self.q = [None] * size
        self.front = -1
        self.rear = -1

    def is_full(self):
        return (self.rear + 1) % self.size == self.front

    def is_empty(self):
        return (self.front == -1)

    def enqueue(self, val):
        if (self.is_full()):
            print("Queue is full")
            return

        if (self.is_empty()):
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size

        self.q[self.rear] = val

    def dequeue(self):
        if (self.is_empty()):
            print("Queue is empty")
            return

        val = self.q[self.front] 

        if (self.front == self.rear):
            self.front = self.rear = 0
        else:
            self.front = (self.front + 1) % self.size

        return val

    def print(self):
        if (self.is_empty()):
            print("Queue is empty")
            return

        i = self.front

        while True:
            print(self.q[i])

            if i == self.rear:
                break

            i = (i + 1)% self.size

c = CircularQueue(5)
c.enqueue(1)
c.enqueue(2)
c.enqueue(3)
c.enqueue(4)
c.enqueue(5)
c.print()
c.dequeue()
c.print()


