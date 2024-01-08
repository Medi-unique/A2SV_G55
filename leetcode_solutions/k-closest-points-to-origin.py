class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res=[]
        def check(num1,num2):
            if num1[0]**2+num1[1]**2 >=  num2[0]**2+num2[1]**2:
                return 1
            elif num1[0]**2+num1[1]**2 <  num2[0]**2+num2[1]**2:
                return -1
            else:
                return 0
        points.sort(key=cmp_to_key(check))
        for i in range(k):
            res.append(points[i])
        return res

        