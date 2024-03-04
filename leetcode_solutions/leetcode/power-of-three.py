class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        def helper(num):
            if num==0: return False
            if num == 1: return True
            if num%3 == 0:
                return helper(num/3)
        return helper(n)
        