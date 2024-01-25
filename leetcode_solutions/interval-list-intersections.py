class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        up,down=0,0
        u=len(firstList)
        d=len(secondList)
        res=[]
        while up < u and down <d:
            ul,ur=firstList[up]
            dl,dr=secondList[down]
            left=max(ul,dl)
            right=min(ur,dr)
            if left<=right:
                res.append([left,right])
            if ur>=dr:
                down+=1
            else:
                up+=1
            
            
        return  res

        