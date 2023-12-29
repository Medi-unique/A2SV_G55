class Solution:
    def sortSentence(self, s: str) -> str:

        words=s.split()
        new=['']*len(words)
        
        for w in words:
            new[int(w[-1])-1]=w[:-1]
        return " ".join(new)