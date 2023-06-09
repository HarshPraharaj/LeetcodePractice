## Maintain two pointers and check two sum for them. Increment/Decrement left and right pointer based on the two_sum

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        l = 0
        r = len(numbers) - 1

        while l <= r:
            
            two_sum = numbers[l] + numbers[r] 
            # print(two_sum)
            if two_sum > target:
                r = r - 1
            elif two_sum < target:
                l = l +1
            else:
                return [l+1,r+1]

        # return -1
