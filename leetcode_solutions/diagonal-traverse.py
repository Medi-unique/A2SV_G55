class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []
        
        rows = len(mat)
        cols = len(mat[0])
        r, c = 0, 0
        up = True
        res = []
        
        while r < rows and c < cols:
            res.append(mat[r][c])
            
            if up:
                if r == 0 or c == cols - 1:
                    up = False
                    if c == cols - 1:
                        r += 1
                    else:
                        c += 1
                else:
                    r -= 1
                    c += 1
            else:
                if c == 0 or r == rows - 1:
                    up = True
                    if r == rows - 1:
                        c += 1
                    else:
                        r += 1
                else:
                    r += 1
                    c -= 1
        
        return res