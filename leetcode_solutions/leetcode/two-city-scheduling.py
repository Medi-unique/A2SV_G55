class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        s=len(costs)  
        scosts = sorted(costs, key=lambda x: -abs(x[0] - x[1]))
        a = b= s//2
        total=0
        for ac , bc in scosts:
            if b==0 or (a and ac<bc):
                total+=ac
                a-=1
            else:
                total+=bc
                b-=1
        return total


        