class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        count,max_s = 0,0
        for num in nums:
            
            if num == 1:
                count+=1
            else:
                max_s = max(max_s,count)
                count=0
        return max(max_s,count)
