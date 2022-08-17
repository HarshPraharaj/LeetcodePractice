
## Approach is to simulate the traversal
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        
        rows = len(matrix)
        cols = len(matrix[0])
        
        dict1 = {}
        
        i,j = 0,0
        spiral_list = []
        
        if cols ==1:
            spiral_list = [list1[0] for list1 in matrix]
            return (spiral_list)
        dir = 'Right'
        while True:
            
            if i<rows and j<cols:
                if (i,j) in dict1.keys():
                    break
                spiral_list.append(matrix[i][j])
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
        print(spiral_list)
        print(i,j)
        return spiral_list
            
