class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        maxi=float('-inf')
        l=0
        map=Counter()
        for r in range(len(s)):
            map[s[r]]+=1
            
            while map[s[r]]>1:
                map[s[l]]-=1
                l+=1
                
            
            maxi=max(maxi,r-l+1)
        return 0 if maxi==float('-inf') else maxi


        