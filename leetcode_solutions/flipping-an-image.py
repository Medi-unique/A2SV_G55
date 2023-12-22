class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for row in image:
            row.reverse()
            for i,r in enumerate(row):
                row[i]=1-row[i]
        return image

        