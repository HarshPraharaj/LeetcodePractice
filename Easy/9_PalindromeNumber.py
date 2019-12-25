class Solution:
    def isPalindrome(self, x: int) -> bool:
        inp = str(x)
        str_copy = inp
        rev = ""
        for i in inp:
            rev = i + rev
        #print(rev)    
        if rev == str_copy:
            return True
        else:
            return False
        
