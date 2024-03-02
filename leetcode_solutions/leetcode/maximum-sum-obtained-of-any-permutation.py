class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n=len(nums)
        temp=[0]* (n+1)

        for start, end in requests:
            temp[start]+=1
            temp[end+1]-=1
        print(temp)

        for i in range(1,len(temp)):
            temp[i]+=temp[i-1]
        print(temp)
        nums.sort(reverse=True)
        temp.sort(reverse=True)
        mod,res= 10**9 + 7,0


        for n,t in zip(nums,temp):
            res += n*t
        return res % mod



        