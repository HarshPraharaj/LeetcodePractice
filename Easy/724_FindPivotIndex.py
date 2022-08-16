class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        num_sums = 0
        
        for i in range(0,len(nums)):
            num_sums += nums[i]
            
            if num_sums - nums[i] == total - num_sums:
                return i
            
        return -1
