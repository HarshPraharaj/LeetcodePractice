class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        ## Method 1 using sum        
        total = sum(nums)
        num_sums = 0
        
        for i in range(0,len(nums)):
            num_sums += nums[i]
            
            if num_sums - nums[i] == total - num_sums:
                return i
            
        return -1

        ## Method 2 Using Slicing
        for i in range(0, len(nums)):
            print(i)
            # print(nums[i],sum(nums[:i]),sum(nums[i:]))
            if sum(nums[:i]) == sum(nums[i+1:]):
                return i
        return -1
      
      
