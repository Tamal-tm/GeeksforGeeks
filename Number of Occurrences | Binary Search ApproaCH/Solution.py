class Solution:
    def countFreq(self, arr, target):
        def findFirst():
            left, right = 0, len(arr) - 1
            first = -1
            while left <= right:
                mid = (left + right) // 2
                if arr[mid] == target:
                    first = mid
                    right = mid - 1   # move left
                elif arr[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return first
        
        def findLast():
            left, right = 0, len(arr) - 1
            last = -1
            while left <= right:
                mid = (left + right) // 2
                if arr[mid] == target:
                    last = mid
                    left = mid + 1    # move right
                elif arr[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return last
            
        lb=findFirst()
        ub=findLast()
        
        if lb == -1:
            return 0
            
        return ub-lb+1
