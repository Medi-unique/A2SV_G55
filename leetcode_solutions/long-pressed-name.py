class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i,j=0,0
        while i<= len(name) and j < len(typed):
            if i< len(name)and name[i]==typed[j]:
                j+=1
                i+=1
            elif name[i-1]==typed[j] and i!=0  :
                j+=1
            else :
                return False
        return i==len(name) and j ==len(typed)
            