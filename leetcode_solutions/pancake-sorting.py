class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        s=len(arr)
        res=[]
        for i in range(s):
            max_ind=arr.index(max(arr[:s-i]))
            arr[:max_ind+1]=arr[:max_ind+1][::-1]
            res.append(max_ind+1)
            arr[:s-i]=arr[:s-i][::-1]
            res.append(s-i)
            
        return res
            