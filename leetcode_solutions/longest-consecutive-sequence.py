class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset=set(nums)
        longest=0
        length=0
        for n in nums:
            # checking of the num hasn't left neghbour
            if n-1  not in numset:
                length=0
                while (n + length) in numset:
                    length+=1
                longest=max(length , longest)
        return longest

