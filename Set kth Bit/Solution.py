#User function Template for python3
class Solution:
	def setKthBit(self, n, k):
		n= n | (1 << k)
		return n
