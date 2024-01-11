class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
      n=len(s1)
      m=len(s2)
      target=Counter(s1)
      first=Counter(s2[:n])  
      if target == first:
          return True
      for i in range(m-n):
          first[s2[i]]-=1
          first[s2[i+n]]+=1
          if first== target:
              return True
      return False
        

