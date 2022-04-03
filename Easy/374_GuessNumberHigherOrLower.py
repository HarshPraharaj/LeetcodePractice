# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        
        low = 1
        high = n
        
        while low <= high:
            
            mid = (low+high)//2
            
            if guess(mid) == 0:
                return mid
            elif guess(mid) == 1:
                low = mid+1
            else:
                high = mid - 1
        
'''        
Runtime: 38 ms, faster than 63.71% of Python3 online submissions for Guess Number Higher or Lower.
Memory Usage: 13.8 MB, less than 97.91% of Python3 online submissions for Guess Number '''
