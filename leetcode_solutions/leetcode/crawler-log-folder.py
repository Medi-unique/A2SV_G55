class Solution:
    def minOperations(self, logs: List[str]) -> int:
        count=0
        for l in logs:
            if l =='./':
                continue
            elif l=='../' :
                if count > 0:
                    count-=1
                else:
                    continue
            else:
                count+=1
        return 0 if count <0 else count

        