class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        curr=cardPoints[:k][::-1]+cardPoints[-1:-1*(k+1):-1]
        n=len(curr)
        first=sum(curr[:k])
        maxi=first
        l=0
        for r in range(k,n):
            first-=curr[l]
            first+=curr[r]
            l+=1
            maxi=max(maxi,first)
        return maxi

        

        