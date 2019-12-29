class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<0:
            return False
        
        if bin(n)[2:].count('1') == 1:
            return True
        else:
            return False
            
            
''' 
1: 0001
2: 0010
4: 0100
8: 1000
'''
