class Solution:
    def subsetSums(self, arr):
        result = []
        
        def solve(index, total):
            if index >= len(arr):
                result.append(total)
                return
            
            Sum = total + arr[index]   # Pick
            solve(index + 1, Sum)
            
            Sum = total                # Not Pick
            solve(index + 1, Sum)
        
        solve(0, 0)
        
        result.sort()
        return result
