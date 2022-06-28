##Using Loop
class Solution:
    def addDigits(self, num: int) -> int:
        
        if num<10:
            return num
        def calc_sum(num):
            sum_digs = 0
            while num>0:
                dig = num %10
                sum_digs +=  dig
                num = num // 10
            return sum_digs
            
        
        while num >= 10:
            num = calc_sum(num)
            
        return num
            
## More efficient method - Digital Roots
class Solution:
    def addDigits(self, num: int) -> int:
        return 1 + (num - 1) % 9 if num else 0
