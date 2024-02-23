class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l=0
        n=len(nums)
        total=0
        maxi=float('-inf')

        for i,r in enumerate(nums):
            print(total,r)

            total+=r

            maxi=max(maxi,total)
            while total < 0 :

                  total -= nums[l]
                  l+=1

        return maxi
        