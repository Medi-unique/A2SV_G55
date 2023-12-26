class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        mydict=defaultdict(int)
        result=[]
        new=[]
        for i in arr2:
            mydict[i]=0
        for j in arr1:
            
            if j in arr2:
                mydict[j] += 1
            else:
                new.append(j)

        combined_list = []
        new.sort()
        print(new)

        for key, value in mydict.items():
            combined_list.extend([key] * value)
        combined_list+=new

        return combined_list

            
        

        