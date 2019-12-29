class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        
        Overlap_X_Left = max(rec1[0],rec2[0])
        Overlap_X_Right = min(rec1[2],rec2[2])
        
        if Overlap_X_Right - Overlap_X_Left <= 0:
            return False
        #else:
            #lenght = Overlap_X_Right - Overlap_X_Left
        
        Overlap_Y_Bot = max(rec1[1],rec2[1])
        Overlap_Y_Top = min(rec1[3],rec2[3])
        
        if Overlap_Y_Top - Overlap_Y_Bot <= 0:
            return False
        #else:
            #breadth = Overlap_Y_Top - Overlap_Y_Bot
            
        return True
