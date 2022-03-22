// Brute Force Method

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = re.sub(r'\W+', '', s). #By Python definition '\W == [^a-zA-Z0-9_], which excludes all numbers, letters and _
        s = s.replace("_","")
        s = s.lower()
        
        rev_s = ""
        
        for i in s:
            rev_s = i + rev_s
        
        if rev_s == s:
            return True
        else:
            return False
