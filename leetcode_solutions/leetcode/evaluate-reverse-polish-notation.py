class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators=['+','-','*','/']
        stack=[]
        for t in tokens:
            
            if t in operators:
                if stack and t=='+':
                    val=stack.pop()
                    stack[-1]+=val
                elif t=='-':
                    val=stack.pop()
                    stack[-1] -=val
                elif t=='*':
                    val=stack.pop()
                    stack[-1] *=val
                elif  t=='/':
                    val=stack.pop()
                    stack[-1] /=val
                    if stack[-1] <0:
                        stack[-1]=ceil(stack[-1])
                    else:
                        stack[-1]=floor(stack[-1])
            else:
                stack.append(int(t))
        return stack[-1]