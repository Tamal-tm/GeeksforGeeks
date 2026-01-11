'''
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
        self.prev = None
'''
class Solution:
    def removeDuplicates(self, head):
        temp = head

        while temp is not None and temp.next is not None:
            if temp.data == temp.next.data:
                dup = temp.next
                temp.next = dup.next
                if dup.next is not None:
                    dup.next.prev = temp
            else:
                temp = temp.next

        return head

                
            
