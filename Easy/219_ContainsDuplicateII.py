## Maintain and traverse in sizes of k (window size) and check if there's a duplicate item

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l = 0
        window_set = set()

        for r in range(len(nums)):
            if r-l>k:
                window_set.remove(nums[l])
                l+=1
            
            if nums[r] in window_set:
                return True
            
            window_set.add(nums[r])
        return False
