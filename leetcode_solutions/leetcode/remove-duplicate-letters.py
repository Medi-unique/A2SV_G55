class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        count=Counter(s)
        stack=[]
        visited=set()

        for l in s:

            count[l]-=1
            while stack and count[stack[-1]] >0 and l not in visited and stack[-1] >= l :
                
                prev=stack.pop()
                visited.remove(prev)
            
            if l not in visited:
                stack.append(l)
                print(visited)
                visited.add(l)
        
        return ''.join(stack)


        