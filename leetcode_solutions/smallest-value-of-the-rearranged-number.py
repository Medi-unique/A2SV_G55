class Solution:
    def smallestNumber(self, num: int) -> int:
        if num>0:
            num=str(num)
            num=sorted(num)
            nums=list(map(int,num))
            j=1
            if nums[0]==0:
                while nums[j]==0:
                      j+=1
                nums[0],nums[j]=nums[j],nums[0]

            ret="".join(map(str,nums))
            
            return int(ret)

        elif num<0:
            num=str(num)
            num=num[1:]
            num=sorted(num,reverse=True)
            nums=list(map(int,num))
            
            ret="".join(map(str,nums))
            
            return -int(ret)
        else:
            return 0
        