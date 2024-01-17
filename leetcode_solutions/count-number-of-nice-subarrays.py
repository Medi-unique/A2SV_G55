class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        new=[0]
        for i,num in enumerate(nums):
            new.append(num%2+new[-1])
        count=Counter(new)
        ans=0
        for n in new:
            ans+=count[n-k]
            
            

        return ans
        
       