# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

## Check for the first TRUE or last FALSE

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        low = 1
        high = n
        
        while low<=high:
            
            mid = (low+high)//2
            
            if isBadVersion(mid):
                if not isBadVersion(mid-1):
                    return mid
                high = mid - 1
            else:
                if isBadVersion(mid+1):
                    return mid+1
                low = mid + 1
            
        
