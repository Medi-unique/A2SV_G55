class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n=len(s)
        l=0
        maxx=0
        res=0
        window=Counter()
        for r in range(n):
            window[s[r]]+=1
            maxx=max(maxx,window[s[r]])
            if (r-l+1) -maxx>k:
                window[s[l]]-=1
                l+=1

            res=max(res,r-l+1)
        return res
























        # res=0
        # for r in range(n):
        #     if s[r] != s[l]:
        #         c+=1
        #     if r==n-1 and c<=k:
        #         res=r-l+1
            
        #     while l<r and( c>k or r==n-1):
        #         res=max(res,r-l)
        #         if s[r] != s[l]:
        #             c-=1
                

        #         l+=1
        # return res 

        