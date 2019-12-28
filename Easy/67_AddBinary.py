class Solution:
    
    def addBinary(self, a: str, b: str) -> str:
        
        list1 = [int(x) for x in str(a)]
        list2 = [int(x) for x in str(b)]
        carry = 0
        num1,num2=0,0
        
        if int(a)==0 and int(b) ==0:
            return "0"
        
        if int(a)!=1:
            for i in range(0,len(list1)):
                num1 = num1 + ( 2**((len(list1) - i)-1) )*list1[i]
        else:
            num1 = 1
            
            
        if int(b)!=1:
            for j in range(0,len(list2)):
                num2 = num2 + ( 2**((len(list2) - j)-1) )*list2[j]
        else:
            num2 = 1
        
        res = num1 + num2
        list3 =[]
        
        while res>0:
            dig = res % 2
            list3.append(dig)
            res = res // 2
        
        op = ""
        for i in reversed(range(len(list3))):
            op = op + str(list3[i])
            #print(op)
            
        return op           
            
            
        
            
        
        
