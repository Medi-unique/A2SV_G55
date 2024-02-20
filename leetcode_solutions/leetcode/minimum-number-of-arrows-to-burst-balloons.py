class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        pre=points[0][1]
        count=len(points)
        for start,end in points[1:]:
            if start <= pre:
                pre=min(pre,end)
                count-=1
            else:
                pre=end
        return count




        