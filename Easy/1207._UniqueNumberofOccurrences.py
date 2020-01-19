class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        dict1 = {}
        freq = []
        
        for i in arr:
            if i in dict1:
                pass
            else:
                dict1[i] = arr.count(i)
                
        for k in dict1:
            if dict1[k] not in freq:
                freq.append(dict1[k])
            else:
                return False
        return True
        
