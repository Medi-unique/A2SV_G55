class Solution:
    def isValid(self, s: str) -> bool:
        check={')':'(','}':'{',']':'['}
        stack=[]
        for l in s:
            if l in check.values():
                stack.append(l)
            else:
                if stack and stack[-1] == check[l]:
                   stack.pop()
                else:
                 return False
        return  True if not stack  else False
