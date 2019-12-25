class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        
        cnt = 0
        
        for i in nums:
            num_digits = 0
            while(i>0):
                num_digits += 1
                i = i//10
            
            if num_digits%2==0:
                cnt += 1
        return cnt
