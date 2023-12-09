class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        steps=0
        current_capacity=capacity
        for i in range(len(plants)):
            if current_capacity<plants[i]:
                steps += i*2
                current_capacity=capacity
            steps+=1
            current_capacity=current_capacity-plants[i]

        return steps