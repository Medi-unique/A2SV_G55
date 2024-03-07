class Solution:
    def hIndex(self, citations: List[int]) -> int:
        l,r=0,max(citations)
        n=len(citations)

        def check(mid):
            count=0
            for val in citations:
                if val >= mid:
                    count+=1
            return count

            
        while l <= r:
            mid=(l+r)//2
            curr=check(mid)

            if curr >= mid:
                l=mid+1

        
            else:
                r=mid-1
        return r


























        # if n==1 and citations[0] == 0:
        #     return 0
        

        # while l<=r:
        #     if citations[0] >= n:
        #         return n
        
        #     mid=(l+r)//2

        #     if citations[mid]> (n-l):
        #         r=mid-1
        #     elif citations[mid] < (n-l):
        #         l=mid+1
        #     else:
        #         return citations[mid]
        # return citations[r]
        