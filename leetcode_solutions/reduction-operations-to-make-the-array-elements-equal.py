class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        arranged=sorted(nums ,reverse=True)
        ans=0
        for i in range(len(arranged)-1):
            if arranged[i]>arranged[i+1]:
                ans+=i+1
        return ans
