class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        l,r=0,0
        res=[]
        for i,v in enumerate(s):
            cur=s.rindex(v)
            if  r < cur:
                r=cur
            if r==i:
                res.append(r-l+1)
                l=r+1
            
        return res



        
        