class myQueue:
    def __init__(self, n):
        self.items = []
        self.capacity = n

    def isEmpty(self):
        return len(self.items) == 0

    def isFull(self):
        return len(self.items) == self.capacity

    def enqueue(self, x):
        if self.isFull():
            return   # ignore if full
        self.items.append(x)

    def dequeue(self):
        if self.isEmpty():
            return   # queries are valid, so safe
        return self.items.pop(0)

    def getFront(self):
        if self.isEmpty():
            return -1
        return self.items[0]

    def getRear(self):
        if self.isEmpty():
            return -1
        return self.items[-1]
