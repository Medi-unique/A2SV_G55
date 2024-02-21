class Solution:
    def longestPalindrome(self, s: str) -> int:
        count=Counter(s)
        res=0
        curr=0
        f=False
        for key,value in count.items():
            if value%2 ==1:
                res+=value-1
                f=True
            else:
                res+=value
        if f :
            res+=1
        return res


                
                
            

        