class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        
        Overlap_X_Left = max(A,E)
        Overlap_X_Right = min(C,G)
        

        lenght = Overlap_X_Right - Overlap_X_Left
        
        Overlap_Y_Bot = max(B,F)
        Overlap_Y_Top = min(D,H)
        
        breadth = Overlap_Y_Top - Overlap_Y_Bot
        
        if lenght<0 or breadth<0:
            return ((C-A)*(D-B)) + ((G-E)*(H-F))
        else:
            return ((C-A)*(D-B)) + ((G-E)*(H-F)) - (lenght*breadth)
        
        
        
