class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        zeros=0
        maxi=float('-inf')
        l=0
        for r,val in enumerate(nums):
            if val==0:
                zeros+=1
                if zeros >k:
                    while nums[l]!=0:
                        l+=1
                    l+=1
            maxi=max(maxi,r-l+1)
        return maxi
            












        