class Solution:
    def romanToInt(self, s: str) -> int:
        dict1 = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000,".":0}
        
        s=s+"."
        total = 0
        i = 0
        while(i<len(s)-1):
            #print(s[i])
            if dict1[s[i+1]] == "." :
                break
            
            elif dict1[s[i]] < dict1[s[i+1]]:
                total = total - dict1[s[i]] + dict1[s[i+1]]
                i = i+2
            

            
            elif dict1[s[i]] > dict1[s[i+1]]:
                total = total + dict1[s[i]] 
                i=i+1
                
            elif s[i] == 'I' or s[i] == 'X' or s[i] == 'C' or s[i] == 'M':
                total = total+dict1[s[i]]
                i=i+1
            #print(total)
        return total
