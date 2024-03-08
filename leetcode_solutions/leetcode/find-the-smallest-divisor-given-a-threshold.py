class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l,r=1,max(nums)
        def check(mid):
            total=0
            for num in nums:
                total += ceil(num/mid)
            return total



        while l <= r:
            mid=(l+r)//2
            curr=check(mid)
            
            if curr > threshold:
                l=mid+1
            else:
                r=mid-1
        return l

        