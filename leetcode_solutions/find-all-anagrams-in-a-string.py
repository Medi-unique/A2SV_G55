class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        l=len(p)
        r=len(s)
        res=[]
        check=Counter(p)
        curr=Counter(s[:len(p)])
        if curr==check:
            res.append(0)
        for i in range(l,r):
            curr[s[i-l]]-=1

            if curr[s[i-l]]==0:
                del(curr[s[i-l]])
            curr[s[i]]+=1
            if curr==check:
                res.append(i-l+1)
               
        return res





        
       
        