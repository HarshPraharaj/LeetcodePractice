class Solution:
    def isHappy(self, n: int) -> bool:
        sum_set = set()
        def calc_sum_digs(num):
            sum_digs = 0
            while num > 0:
                dig = num % 10
                sum_digs = sum_digs + (dig*dig)
                num = num // 10
            return sum_digs
        
        while n not in sum_set:
            sum_set.add(n)
            n = calc_sum_digs(n)
            if n == 1:
                return True
        return False
        
## Maintain a set to see if a "Sum" has been obtained before --> If yes, implies that we are stuck in a cycle
