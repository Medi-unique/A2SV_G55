class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pref=[0]
        res=0
        for num in nums:
            pref.append(num+pref[-1])
        count=Counter()
        summ=0
        for p in pref:
            res+=count[p]
            count[p+k]+=1
        return res



