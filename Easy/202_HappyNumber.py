class Solution:
    def isHappy(self, n: int) -> bool:
        def squareNumber(n):
            sum1 = 0
            while(n>0):
                dig = n % 10
                sum1 = sum1 +(dig*dig)
                n = n//10
            return sum1
        
        
        while True:
            ans = squareNumber(n)
            if ans == 1:
                return True
            elif ans < 10:
                return False
            else:
                n = ans


        
        
        

            

            
        
