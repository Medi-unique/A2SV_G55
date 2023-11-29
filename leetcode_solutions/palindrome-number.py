class Solution:
    def isPalindrome(self, x: int) -> bool:
        y=str(x)
        reverse=y[::-1]
        return y==reverse
       
           
        