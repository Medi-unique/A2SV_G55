class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        my=list(s)
        n=len(s)
        for i in range(0,n,2*k):
            start=i
            end=min(n,i+k)
            my[start:end]=reversed(my[start:end])
        res="".join(my)
        return res
        