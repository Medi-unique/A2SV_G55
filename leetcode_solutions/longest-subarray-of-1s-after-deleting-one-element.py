class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        s=len(nums)
        l=0
        count=0
        res=0
        for r in range(s):
            if nums[r]==0:
                count+=1

                if  count>1:
                    while nums[l] != 0 and l<r:
                        print(l)
                        l+=1
                    count-=1
                    l+=1
            res=max(res,r-l)
        return res

        

            