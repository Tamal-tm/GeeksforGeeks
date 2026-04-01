# Node class
class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None


# Queue class
class myQueue:

    def __init__(self):
        self.front = None
        self.rear = None
        self.count = 0

    def isEmpty(self):
        return self.front is None

    def enqueue(self, x):
        new_node = Node(x)

        if self.rear is None:  # queue is empty
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

        self.count += 1

    def dequeue(self):
        if self.front is None:
            return -1

        temp = self.front
        self.front = self.front.next

        # If queue becomes empty
        if self.front is None:
            self.rear = None

        self.count -= 1
        return temp.data

    def getFront(self):
        if self.front is None:
            return -1
        return self.front.data

    def size(self):
        return self.count
