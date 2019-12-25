class Solution:
    def isValid(self, s: str) -> bool:
        
        isBalanced = False
        st = []
        if s is "":
            return True
        
        for i in s:
            if i is '(' or i is '{' or i is '[' :
                st.append(i)
                #print(st)
            else:
                if len(st)==0:
                    isBalanced = False
                else:
                    top = st.pop()
                    print("Open",top)
                    print("close",i)
                    if top == "(" and i == ")":
                        isBalanced = True
                    elif top == "{" and i == "}":
                        isBalanced = True
                    elif top == "[" and i == "]":
                        isBalanced = True
                    else:
                        isBalanced = False
                        break
        
        if len(st) is not 0:
            return False
        return isBalanced
                
        
