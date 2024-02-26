class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        r=rowIndex
        
        
        def pascal(r):
            
            if r == 0: return [1]
            if r == 1: return [1,1] 

            new=pascal(r-1)
            curr=[1]
            for i in range(1,len(new)):
                curr.append(new[i]+new[i-1])
            curr.append(1)
            return curr
        return pascal(r)

        