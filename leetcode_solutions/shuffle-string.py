class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        zipped=dict(zip(indices,s))
        sor=dict(sorted(zipped.items()))
       
        res=''.join(sor.values())
       
        return res