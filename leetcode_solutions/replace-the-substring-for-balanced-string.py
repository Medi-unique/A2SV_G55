class Solution:
    def balancedString(self, s: str) -> int:
        n=len(s)
        l=0
        check=''
        res=float('inf')
        count=Counter(s)
        for k,v in count.items():
            if v>n//4:
                check+=k*(v-n//4)
        replace= Counter(check)
        print(replace)
        h=0
        c=len(replace)
        window=Counter()
        if not check:
            return 0
      
        for r in range(n):
            window[s[r]]+=1
            if s[r] in replace and window[s[r]]==replace[s[r]]:
                h+=1
            while h==c:
                res=min(r-l+1,res)
                window[s[l]]-=1
                if s[l] in replace and  window[s[l]] <replace[s[l]]:
                    h-=1

                l+=1

        return res if res!= float('inf') else 0


        