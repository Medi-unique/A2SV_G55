class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        pref=[0]
        for num in nums:
            pref.append(num+pref[-1] %k)
       
        mod=[num%k for num in pref]
        count=Counter()
      
        res=0
        for val in mod:
            res+=count[val]
            count[val]+=1

        return res
        