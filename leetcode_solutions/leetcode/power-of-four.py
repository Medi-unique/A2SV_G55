class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        def helper(num):
            if num == 0 : return False
            if num == 1: return True
            if num % 4 ==0:
                return helper(num/4)
        return helper(n)
        