class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        res=[]
        maxi=0
        for i in points:
            res.append(i[0])
        res.sort()
        for j in range(len(res)-1):
            if res[j+1]-res[j]>maxi:
                maxi=res[j+1]-res[j]
        return maxi
