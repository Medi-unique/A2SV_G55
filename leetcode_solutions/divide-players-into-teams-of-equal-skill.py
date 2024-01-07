class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        
        skill.sort()
        i,j,res=0,len(skill)-1,0
        while i<j:
            check=skill[0]+skill[-1]
            if skill[i]+skill[j]==check:
                res+=skill[i]*skill[j]
                i+=1
                j-=1
            else:
                return -1
        return res
