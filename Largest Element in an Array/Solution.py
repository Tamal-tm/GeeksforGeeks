class Solution:
    def largest(self, arr):
        largest=float("-inf")
        n=len(arr)
        for i in range(0,n):
            largest=max(largest,arr[i])
        
        return largest
        

