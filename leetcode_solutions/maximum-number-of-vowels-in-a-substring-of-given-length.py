class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        t=len(s)
        vowels=('a','e','o','u','i')
        check=s[:k]
        count=0
        l=0
        for i in check:
                if i in vowels:
                    count+=1
                if count==k:
                    return count
        maxi=count
        print(count,t)

        for r in range(k,t):
            if s[r]in vowels:
                count+=1
            if s[l] in vowels:
                count-=1
            l+=1
            print(count,r,l)
            maxi=max(maxi,count)
        return maxi          

            
            
                
            
                
                 
                    
        