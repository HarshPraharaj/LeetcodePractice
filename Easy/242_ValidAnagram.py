class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        dict1 =  {}
        dict2 = {}
        #print(len(s),len(t))
        if len(s) != len(t):
            #print("NW")
            return False
        
        
        for i in s:
            if i in dict1:
                dict1[i] += 1
            else:
                dict1[i] = 1
        
        for j in t:
            if j in dict2:
                dict2[j] += 1
            else:
                dict2[j] = 1
       
    
        op = True
        print(dict1)
        print(dict2)
        
        for k in t:
            if k not in s:
                print(i)
                return False
            else:
                if dict1[k] == dict2[k]:
                    op = True
                    #print(dict1[i],dict2[i],op)
                else:
                    return False
        return op
            
                    
            
        
