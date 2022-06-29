''' Runtime: 28 ms, faster than 77.31% of Python3 online submissions for Ugly Number.
Memory Usage: 13 MB, less than 100.00% of Python3 online submissions for Ugly Number.
'''


#BRUTE FORCE APPROACH

class Solution:
    def isUgly(self, num: int) -> bool:
        if num ==0:
            return False
        
        while num!=1:
            if num % 5 ==0:
                num = num /5
            elif num % 3 ==0:
                num = num/3
            elif num %2==0:
                num = num/2
            else:
                break
        if num ==1:
            return True
        else:
            return False
          
## Alternate Approach
class Solution:
    def isUgly(self, n: int) -> bool:
        if n == 0:
            return False
        for i in [5,3,2]:
            
            while n % i == 0:
                n = n / i
        if n == 1:
            return True
        else:
            return False
