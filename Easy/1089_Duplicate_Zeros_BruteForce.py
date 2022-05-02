# Not an efficient Solution
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        
        i = len(arr) - 1
        
        while i >= 0:
            if arr[i] == 0:
                
                for j in range(len(arr)-1,i,-1):
                    
                    arr[j] = arr[j-1]
            i -= 1
                    
                
