#User function Template for python3
class Solution:
	def perfectSum(self, arr, target):
		def backtrack(index,total):
		    if index == len(arr):
                if total == target:
                    return 1
                return 0
		    if index >= len(arr):
		        return 0
            summ=total+arr[index]
            pick=backtrack(index+1,summ)
            summ=total
            not_pick=backtrack(index+1,summ)
            return pick+not_pick
    
        return backtrack(0,0)
        
