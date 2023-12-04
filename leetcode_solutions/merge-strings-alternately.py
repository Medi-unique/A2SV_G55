class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result=""
        short=min(len(word1),len(word2))
        for i in range(short):
            result +=word1[i]
            result+=word2[i]
        result +=word1[short:]
        result +=word2[short:]
        return result
        
        