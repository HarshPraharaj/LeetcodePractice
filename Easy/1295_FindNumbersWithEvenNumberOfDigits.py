class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        
        def number_of_digits(num):
            
            count=0
            while num > 0:
                dig = num % 10
                count+=1
                num = num//10
            return count
        
        count_total = 0
        for num in nums:
            count = number_of_digits(num)
            # print(num,count)
            if count % 2 == 0:
                count_total += 1
                
        return count_total
        
