class Solution:
    def bitManipulation(self, num, i):
        bit = i - 1   # convert to 0-based indexing
        
        # 1. Get ith bit
        get_bit = (num >> bit) & 1
        
        # 2. Set ith bit
        set_bit = num | (1 << bit)
        
        # 3. Clear ith bit
        clear_bit = num & ~(1 << bit)
        
        print(get_bit, set_bit, clear_bit)
