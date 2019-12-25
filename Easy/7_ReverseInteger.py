
class Solution:
    def reverse(self, x: int) -> int:

        num = x
        new_num = 0
        if num < 0:
            x = x*-1
        
        while(x>0):
            dig = x % 10
            new_num = new_num*10 + dig

            x = x // 10
    
    
        if new_num > 2**31:
            return 0
        elif new_num < -2**31:
            return 0
        elif num < 0:
            return ( new_num*-1)
        else:
            return new_num
