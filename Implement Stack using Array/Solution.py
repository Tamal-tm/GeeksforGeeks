class myStack:
    def __init__(self, n):
        self.items = []
        self.capacity = n   # store max size

    def isEmpty(self):
        return len(self.items) == 0

    def isFull(self):
        return len(self.items) == self.capacity

    def push(self, x):
        if self.isFull():
            return   # or ignore as per problem
        self.items.append(x)

    def pop(self):
        if self.isEmpty():
            return   # as per problem, queries are valid
        return self.items.pop()

    def peek(self):
        if self.isEmpty():
            return -1
        return self.items[-1]
