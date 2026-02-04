#User function Template for python3

class Solution:
    def checkSubsequenceSum(self, N, arr, K):
        def backtrack(index, total, subset):
            if total == K: 
                return True
            elif total > K:
                return False
            if index >=len(arr):
                return False
            
            # Pick
            subset.append(arr[index])
            summ=total+arr[index]
            pick=backtrack(index+1,summ,subset)
            if pick == True:
                return True
            
            # Not Pick
            subset.pop()
            summ=total
            not_pick=backtrack(index+1,summ,subset)
            return not_pick
        
        return backtrack(0,0,[])
