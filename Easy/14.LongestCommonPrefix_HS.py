// Using Horizontol Scanning

class Solution:
            
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        def find_common(a,b):
            prefix = ""
            min_len = min(len(a),len(b))
            for i in range(0,min_len):
                if a[i] == b[i]:
                    prefix = prefix + a[i]
                else:
                    return prefix
            return prefix
        
        strs = sorted(strs)
        prefix = strs[0]
        for i in range(0,len(strs)-1):
            prefix = find_common(prefix,strs[i+1])
        return prefix
                
    
