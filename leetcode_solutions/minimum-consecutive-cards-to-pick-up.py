class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        check=Counter()
        
        n=len(cards)
        l=0
        mini=float('inf')
        for r in range(n):
            check[cards[r]]+=1
            while check[cards[r]]==2:
                  mini=min(r-l+1,mini)
                  check[cards[l]]-=1
                  if check[cards[l]]==0:
                      del(check[cards[l]])
                  l+=1
            # mini=min(r-l+1,mini)
        return mini if mini!=float('inf') else -1




        