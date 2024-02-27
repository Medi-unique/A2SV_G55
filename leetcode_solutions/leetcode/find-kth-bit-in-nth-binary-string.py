class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def revInv(nums):
            res=[]
            for n in nums:
                if n=='1':
                    res.append('0')
                else:
                    res.append('1')
                
            return ''.join(res[::-1])
        # print(revInv('001'))
        def helper(n):
            curr=''
        
            if n==1: return '0'

            curr = helper(n-1)
            return curr +'1'+ revInv(curr)


        res=helper(n)
        return res[k-1]
    
        
