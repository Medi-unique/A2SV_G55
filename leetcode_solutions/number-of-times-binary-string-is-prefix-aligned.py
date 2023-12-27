class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        count = 0  
        max_index = 0  #  maximum index flipped
        
        for i, v in enumerate(flips):
            max_index = max(max_index, v)  
            
            if max_index == i + 1:  
                count += 1 
        
        return count