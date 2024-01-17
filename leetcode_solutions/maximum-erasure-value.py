class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        score=0
        maxi=0
        l=0
        n=len(nums)
        check=set()
        for r in range(n):
            while nums[r] in check:
                score-=nums[l]
                check.remove(nums[l])
                l+=1
            check.add(nums[r])
            score+=nums[r]
            maxi=max(maxi,score)
        return maxi
                


