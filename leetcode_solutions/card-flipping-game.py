class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        full=set(fronts + backs)
        forbidden=set()
        res=float('inf')
        for (i,f),(j,b) in zip(enumerate(fronts),enumerate(backs)):
            if f==b:
                forbidden.add(f)
        if len(full-forbidden) != 0:
            res=min(full-forbidden)
        
        return res if res !=  float('inf') else 0