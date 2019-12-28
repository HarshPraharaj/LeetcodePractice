import math
class Solution:
    def convertToTitle(self, n: int) -> str:
        op = ""
        while n > 0:
            if n % 26 == 0:
                op = "Z" + op
                n = n // 26 - 1
            else:
                op = chr(64 + n % 26) + op
                n = n // 26
    
        return op
''' 
        op = ""
        
        if n ==702:
            return "ZZ"
        
        if n <=26:
            return chr(n+64)
        while n>26:
            dig = n // 26
            dig1 = n % 26
            if n % 26 != 0:                
                op = op + chr(dig+64) + chr(dig1+64)
                n = n // 26
            else:
                op = op + chr(dig+63) + "Z"
                n = (n//26) -1
        
        return op
    '''        
