class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        mini=0
        n=len(blocks)
        first=Counter(blocks[:k])
        mini=first['W']
        # print(mini)
        l=0
        for r in range(k,n):
            first[blocks[l]]-=1
            first[blocks[r]]+=1
            l+=1
            
            if first['W']<mini:
                mini=first['W']
                
        return mini


            
        