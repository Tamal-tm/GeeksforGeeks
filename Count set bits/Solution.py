class Solution:
    def countSetBits(self, n):
        count = 0
        i = 1
        
        while i <= n:
            full_cycles = (n + 1) // (i * 2)
            count += full_cycles * i
            
            remainder = (n + 1) % (i * 2)
            count += max(0, remainder - i)
            
            i <<= 1
        
        return count
