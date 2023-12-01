class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        num1=(num-3)//3
        
        result=[]
        if (num-3)%3 ==0:
            result.append(num1) 
            result.append(num1+1)    
            result.append(num1+2)    
        return result
            
        
    
            
        