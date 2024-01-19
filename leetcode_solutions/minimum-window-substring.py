class Solution:
    def minWindow(self, s: str, t: str) -> str:
        check=Counter(t)
        c=len(check)
        have=0
        n=len(s)
        reslen=float('inf')
        res=[-1,-1]
        l=0
        window=Counter()
        for r in range(n):
            window[s[r]]+=1
            if s[r] in check and check[s[r]]==window[s[r]]:
                have+=1

            while have==c:
                # res=[l,r]
                
                # reslen=min(r-l+1,reslen)
                if r-l+1 < reslen:
                    reslen=r-l+1
                    res=[l,r]
                window[s[l]]-=1
                if s[l] in check and window[s[l]]<check[s[l]]:
                    have-=1
                l+=1
        return "" if reslen==float('inf') else s[res[0]:res[1]+1]
                



        