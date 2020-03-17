class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

        dict1 = {}
        n = nums[:]
        
        nums.sort()
        
        for i in range(len(nums)):
            if i == 0 or nums[i-1] < nums[i]:
                dict1[nums[i]] = i
        
        return [dict1[num] for num in n]
