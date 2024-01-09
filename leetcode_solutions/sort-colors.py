class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # for i in range(len(nums)):
        #    for j in range(len(nums)-1):
        #        if nums[j]>nums[j+1]:
        #            nums[j],nums[j+1]=nums[j+1],nums[j]
        n = len(nums)
        i = 0
        j = 0
        k = n - 1
        #i-0  j-1  k-2

        while j <= k:
            if nums[j] == 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
            elif nums[j] == 2:
                nums[j], nums[k] = nums[k], nums[j]
                k -= 1
            else:
                j += 1
              





