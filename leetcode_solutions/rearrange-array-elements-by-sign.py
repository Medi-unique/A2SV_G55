class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos,neg,res=[],[],[]
        for i in nums:
            if i<0:
                neg.append(i)
            else :
                pos.append(i)
        # print(pos,neg)
        maximum=max(len(pos),len(neg))
        for i in range(maximum):
            if i < len(pos):
                res.append(pos[i])
            if i< len(neg):
                res.append(neg[i])
        return res
        
        