class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        rows=len(strs)
        cols=len(strs[0])
        count=0
        for c in range(cols):
            curr=[]
            for r in range(rows):
                curr.append(strs[r][c])
            print(curr)
            if curr != sorted(curr):
                count+=1
        return count