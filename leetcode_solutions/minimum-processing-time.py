class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort(reverse=True)
        tasks.sort()
        large=float('-inf')
        j=0
        # for i in range(len(tasks)):
        for i in range(3,len(tasks),4):
            large=max(tasks[i]+processorTime[j],large)
            j+=1
        return large
        