class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        
        que= deque(range(len(tickets)))
        ans=0

        while tickets[k]!=0:
            val=que.popleft()
            
            if tickets[val] >0:
                tickets[val]-=1
                ans+=1
            que.append(val)

        return ans                

        


        