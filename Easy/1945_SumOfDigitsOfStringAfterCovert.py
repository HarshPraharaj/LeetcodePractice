class Solution:
    def getLucky(self, s: str, k: int) -> int:

        def convert_to_int(s):
            new_s = ""
            for i in s:
                new_s = new_s + str(ord(i)-96)
            return int(new_s)
        
        s = convert_to_int(s)
        
        def sum_of_digits(s,k):
            
            while k>0:
                sum_digs = 0
                while s > 0:
                    dig = s % 10
                    sum_digs += dig
                    s = s // 10
                s = sum_digs
                k = k - 1
            return sum_digs
        return(sum_of_digits(s,k))
        
