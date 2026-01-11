#User function Template for python3
'''
# Node Class
    class Node:
        def __init__(self, data):   # data -> value stored in node
            self.data = data
            self.next = None
            self.prev = None
'''
class Solution:
    def deleteAllOccurOfX(self, head, x):
        temp = head
        new_head = head

        while temp is not None:
            next_node = temp.next

            if temp.data == x:
                # If deleting head
                if temp.prev is None:
                    new_head = temp.next
                    if new_head:
                        new_head.prev = None
                else:
                    temp.prev.next = temp.next
                    if temp.next:
                        temp.next.prev = temp.prev

            temp = next_node

        return new_head
