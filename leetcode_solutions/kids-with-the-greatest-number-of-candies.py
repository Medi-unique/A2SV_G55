class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result=[]
        for i in candies:
            if (i+extraCandies) < int(max(candies)):
                result.append(False)
            else:
                result.append(True)
        return result
                
        
        