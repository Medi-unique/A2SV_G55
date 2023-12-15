class OrderedStream:

    def __init__(self, n: int):
        self.values={}
        self.ptr=1
        

    def insert(self, idKey: int, value: str) -> List[str]:
        self.values[idKey]=value
        result=[]
        while self.ptr in  self.values:
             result.append(self.values[self.ptr])
             self.ptr+=1
        return result


        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)