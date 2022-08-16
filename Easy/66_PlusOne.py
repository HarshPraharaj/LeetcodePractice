class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ##Efficient Method
        Flag = True
        for i in range(len(digits)-1,-1,-1):
            # print(digits[i])
            if Flag == True:
                if digits[i] == 9:
                    digits[i] = 0
                else:
                    digits[i] += 1
                    Flag = False
        if Flag == True:
            digits.insert(0,1)
        return digits
            
        #Brute Force
        p = len(digits)-1
        # print(type(p))
        num = 0
        for i in digits:
            # print(i)
            num += i*math.pow(10,p)
            # print(num)
            p = p-1
            print(int(num))
        new_num = str(int(num) +1)
        print(new_num)
        
        f_list = []
        for i in new_num:
            f_list.append(int(i))
        return f_list
        
        
