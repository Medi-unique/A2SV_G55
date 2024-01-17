class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        summ=0
        n=len(nums)
        l=0
        mini=float('inf')
        for r in range(n):
            summ+=nums[r]
            while l<=r and summ>=target:
                mini=min(mini,r-l+1)
                summ-=nums[l]
                l+=1
        return mini if mini!=float('inf') else 0
