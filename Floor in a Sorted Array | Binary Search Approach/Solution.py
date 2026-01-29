class Solution:
    def findFloor(self, arr, x):
        n=len(arr)
        max_val=-1
        low=0
        high=n-1
        while low <=high:
            mid=(low+high)//2
            if arr[mid] <= x: 
                max_val=mid
                low=mid+1
            else:
                high=mid-1
        
        return max_val

        
