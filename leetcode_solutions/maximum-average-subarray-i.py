class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        i,j,lar=0,k,float('-inf')
        tot=sum(nums[0:k])
        print(tot)
        while j < len(nums):
              lar=max(lar,tot/k)
              tot-=nums[i]
              tot+=nums[j]
              print(tot)
              i+=1
              j+=1
            
        return max(lar,tot/k)

        
        