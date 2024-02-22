class Solution:
    def minimumSteps(self, s: str) -> int:
        size=len(s)
        l,r=0,size-1
        s1=list(s)
        count=0
        while l<r:
            if s1[r]=='0' and s1[l]=='1':
                s1[r],s1[l]=s1[l],s1[r]
                count+=(r-l)
                l+=1
                r-=1
            elif s1[r]=='1' and s1[l]=='1':
                r-=1
            elif s1[r]=='0' and s1[l]=='0':
                
                l+=1
            
            else:
                l+=1
                r-=1
        return count

        
        