class Solution:
    def simplifyPath(self, path: str) -> str:
        path=path.split('/')
        print(path)
        stack=[]
        
        
            
        for p in path:
            if p=='..' :
                if stack:
                
                    stack.pop()
               
            elif p == '.' or p == "":
                continue
            else:
            
            
                stack.append('/'+p)
        return '/' if not stack else ''.join(map(str,stack))