class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        
        t,a = 0,0
        
        l = []
        for i in range(0,len(S)):
            if S[i] == '(':
                t+=1
            else:
                t-=1
            
            
            if t==0:
                l.append(S[a+1:i])
                a = i+1
        new_Str = ""
        
        for i in l:
            new_Str += i
            
        return new_Str
        
