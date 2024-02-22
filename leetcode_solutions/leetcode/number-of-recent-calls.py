class RecentCounter:

    def __init__(self):
        self.que= deque()   

    def ping(self, t: int) -> int:
        s,e=t-3000,t
    
        while self.que and self.que[0] <s:
                  self.que.popleft()
        self.que.append(t)
                  
                
        return len(self.que)


        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)