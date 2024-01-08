class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        large=max(costs)
        arr=[0]*(large+1)
        res=[]
        count,j=0,0
        for i in costs:
            arr[i]+=1
        for j in range(len(arr)):
            if arr[j]>0:
                v=[j]*arr[j]
                res.extend(v)
            else:
                continue
        for k in res:
            coins-=k
            if coins>=0:
                count+=1
            else:
                break



        return count
            

