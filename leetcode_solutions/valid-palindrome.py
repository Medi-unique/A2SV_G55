class Solution:
    def isPalindrome(self, s: str) -> bool:
            #used .join() function to join each letter as a string after checking the letter is alphanumeric and converting to lowercase using .lower() function
       
       
        
        
        s=''.join( char.lower() for char in s if char.isalnum())
        return s ==s[::-1]
            