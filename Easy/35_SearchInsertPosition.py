class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        isFound = False
        
        if target in nums:
            for i in range(0,len(nums)):
                if nums[i]==target:
                    return i
        else:
            if target < nums[0]:
                return 0
            elif target > nums[len(nums)-1]:
                return len(nums)
            else:
                for i in range(1,len(nums)):
                    if target <= nums[i] and target >= nums[i-1]:
                        return i
    
            
        
