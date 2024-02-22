class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures)
        result=[0]*n
        stack=[0]
        curr=0
        for i in range(1,n):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                result[stack[-1]]= i-stack[-1]
                stack.pop()
            stack.append(i)
                
        return result
                




        