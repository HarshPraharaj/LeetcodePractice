class Solution:
    def titleToNumber(self, s: str) -> int:
        l = len(s)
        
        if l <2:
            return ord(s)-64
        
        sum1 = 0
        for i in s:
            sum1 = sum1 + ((ord(i)-64)*(26**(l-1)))
            l -= 1
        return sum1
