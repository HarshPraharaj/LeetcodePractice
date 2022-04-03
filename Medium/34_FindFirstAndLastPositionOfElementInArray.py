class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def findOccurence(nums,target,pos):
            low = 0
            high = len(nums) - 1
            if pos == 'first':
                
                while low <= high:
                    mid = (low+high)//2
                    
                    if nums[mid] == target:
                        if mid <= low:
                            return mid
                        if nums[mid-1] == target:
                            high = mid - 1
                        else:
                            return mid
                    elif nums[mid] > target:
                        high = mid - 1
                    else:
                        low = mid + 1
                return -1
            else:
                while low <= high:
                    mid = (low+high)//2
                    print(mid)
                    if nums[mid] == target:
                        if mid >= high:
                            return mid
                        if nums[mid+1] == target:
                            low = mid + 1
                        else:
                            return mid
                    elif nums[mid] > target:
                        high = mid - 1
                    else:
                        low = mid + 1
                return -1
                
        if len(nums) > 0 :
            first = findOccurence(nums,target,'first')
            last = findOccurence(nums,target,'last')
        else:
            first,last = -1,-1
        l1 = []
        l1.append(first)
        l1.append(last)
        return l1
        
        
'''
Runtime: 163 ms, faster than 13.05% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.
Memory Usage: 15.5 MB, less than 54.54% of Python3 online
'''
