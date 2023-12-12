class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        quarter=len(arr)//4
        for a in arr:
            if arr.count(a)>quarter:
                return a
        