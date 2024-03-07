class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        diff = [[0]*n for _ in range(n)]
        for i in range(n):
            diff[i][i]=nums[i]
        
        for i in range(n-2,-1,-1):
            for j in range(i+1,n):
                diff[i][j] = max(nums[i]-diff[i+1][j],nums[j]-diff[i][j-1])
        
        return diff[0][n-1]>=0