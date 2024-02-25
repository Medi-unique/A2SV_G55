class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        s=len(nums)
        left=0
        total=sum(nums)
        res=[]
        for i,n in enumerate(nums):
            right= total-n-left
            lsize=i
            rsize=s-i-1
            res.append(((n*lsize)-left)+(right-(n*rsize)))
            left+=n
        return res
        