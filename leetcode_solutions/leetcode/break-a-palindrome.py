class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        arr=list(palindrome)
        n=len(palindrome)
        if n==1:
            return ''
        else:
            for i in range(n):
                if arr[i] != 'a' and i != (n)//2 :
                    arr[i]='a'
                    break
            ans=''.join(map(str,arr))
            if ans==palindrome:
                
                arr[-1]='b'

        
        return ''.join(map(str,arr))

        