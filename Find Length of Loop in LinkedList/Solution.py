'''
class Node:
    def __init__(self, data): 
        self.data = data
        self.next = None
'''

class Solution:
    def lengthOfLoop(self, head):
        slow=head
        fast=head
        while fast is not None and fast.next is not None:
            
            slow=slow.next
            fast=fast.next.next
            
            if slow == fast:
                count=1
                slow=slow.next
                while slow!=fast:
                    count +=1
                    slow=slow.next
                return count
        
        return 0
