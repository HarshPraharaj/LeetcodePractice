class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        rows,cols = n,n
        matrix = [ [ 0 for i in range(n) ] for j in range(n) ]
        i,j = 0,0
        print(matrix)
        val = 1
        dir = "Right"
        dict1 = {}
        while True:
            
            if i<rows and j<cols:
                if (i,j) in dict1.keys():
                    break
                matrix[i][j] = (val)
                val+=1
                dict1[i,j] = 1
            else:
                break
            
            if dir == 'Right':
                if j+1 == cols:
                    dir = 'Down'
                    i = i+1
                else:
                    j = j+1
                    if (i,j) in dict1.keys():
                        dir = 'Down'
                        i = i+1
                        j = j-1
                        
            elif dir == 'Down':
                if i+1 == rows:
                    dir = 'Left'
                    j = j-1
                    
                else:
                    i = i+1
                    if (i,j) in dict1.keys():
                        dir = 'Left'
                        i = i -1
                        j = j-1
            
            elif dir == 'Left':
                if j-1 == -1:
                    dir = 'Top'
                    i = i-1
                    
                else:
                    j = j-1
                    if (i,j) in dict1.keys():
                        dir = 'Top'
                        i = i - 1
                        j = j+1

            elif dir == 'Top':
                if i-1 == -1:
                    dir = 'Right'
                    j = j+1
                    # break
                else:
                    i = i-1
                    if (i,j) in dict1.keys():
                        dir = 'Right'
                        i = i +1
                        j = j+1
                    
        print(dict1)
        # print(spiral_list)
        print(i,j)
        return matrix
