class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        count = 0
        modified = False
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                count += 1
                if count > 1:
                    return False
                if i == 1 or nums[i] >= nums[i-2]:
                    nums[i-1] = nums[i]
                else:
                    nums[i] = nums[i-1]
                modified = True
        
        if modified and count == 1 and nums[1] < nums[0]:
            return False
        
        return True