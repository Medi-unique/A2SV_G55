class NumArray:

    def __init__(self, nums: List[int]):
        
        self.prefix=[0]
        for i in range(len(nums)):
            self.prefix.append(nums[i]+self.prefix[-1])

            
            
        

    def sumRange(self, left: int, right: int) -> int:
        left=self.prefix[left]
        right=self.prefix[right+1]
        return right-left
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)