class Solution:
    def defangIPaddr(self, address: str) -> str:
        
        
        newStr = ""
        for i in address:
            if i is '.':
                newStr = newStr + "[.]"
            else:
                newStr = newStr + i
            
        return newStr
