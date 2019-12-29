class Solution:
    def addDigits(self, num: int) -> int:
        
        
        def calculateSum(n):
            sum1 = 0
            while(n>0):
                dig = n %10
                sum1 = sum1 + dig
                n = n//10
            return sum1
        
        while True:
            ans = calculateSum(num)
            if ans <10:
                return ans
            num = ans
