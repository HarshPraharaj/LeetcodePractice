class Solution:
    def countPrimes(self, n: int) -> int:
        
        prime = [ True for i in range(0,n+1)]
        p =2
        
        while p*p <= n:
            if prime[p] == True:
                
                for i in range(p*p,n+1,p):
                    prime[i] = False
                    
                p += 1
        count = 0
        for j in range(2,n):
            if prime[j] is True:
                count+=1
        
        return count
            
