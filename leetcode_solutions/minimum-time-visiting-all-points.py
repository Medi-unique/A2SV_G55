class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        path=0
        for point in range(len(points)-1):
            x,y=points[point]
            m,n=points[point+1]
            horizontal=abs(m-x)
            vertical=abs(n-y)
            diagonal=min(horizontal,vertical)
           
            path +=vertical+horizontal-diagonal
        return path
            
        