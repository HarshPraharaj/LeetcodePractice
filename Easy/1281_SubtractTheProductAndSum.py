class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        
        n1 = n
        sum1=0
        prod1=1
        
        while(n>0):
            dig = n %10
            sum1+=dig
            prod1*=dig
            n = n//10
        
        return prod1-sum1
        
        
