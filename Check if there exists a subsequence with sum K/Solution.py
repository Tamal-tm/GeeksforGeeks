class Solution:
    def checkSubsequenceSum(self, N, arr, K):
        
        def backtrack(index, total):
            # ✅ If we reached required sum
            if total == K:
                return True
            
            # ❌ If sum exceeded or array finished
            if total > K or index == N:
                return False
            
            # 👉 Choice 1: pick current element
            if backtrack(index + 1, total + arr[index]):
                return True
            
            # 👉 Choice 2: do not pick current element
            if backtrack(index + 1, total):
                return True
            
            return False
        
        return backtrack(0, 0)
