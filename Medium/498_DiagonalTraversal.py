class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        
        rows = len(mat)
        cols = len(mat[0])
        
        diagonals = [[] for _ in range(rows+cols-1)]
        # print(diagonals)
        
        for i in range(0, rows):
            for j in range(0, cols):
                diagonals[i+j].append(mat[i][j])
        print(diagonals)
        
        diag_list = []
        
        for i,list1 in enumerate(diagonals):
            if i%2 == 0:
                diag_list.extend(list1[::-1])
            else:
                diag_list.extend(list1)
                
        return (diag_list)
            
