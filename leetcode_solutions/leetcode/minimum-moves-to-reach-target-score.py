class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        curr=target
        count=0
        while curr>1 and maxDoubles:
            if curr%2==1:
                count+=1
                curr-=1
            elif curr%2 !=1 :
                curr //= 2
                count+=1
                maxDoubles-=1
            
        return count + curr-1


        