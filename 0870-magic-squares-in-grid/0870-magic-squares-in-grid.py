class Solution(object):
    def numMagicSquaresInside(self, grid):
        def magic(r,c):
            values = set()
            for i in range(r,r+3):
                for j in range(c,c+3):
                    if grid[i][j] in values or not(1 <= grid[i][j] <=9):
                        return 0
                    values.add(grid[i][j])

            for i in range(r,r+2):
               if  sum(grid[i][c:c+3]) != 15:
                    return 0
            for i in range(c,c+3):
                if (grid[r][i] + grid[r+1][i] + grid[r+2][i])!=15:
                    return 0

            if (
                grid[r][c]+grid[r+1][c+1] + grid[r+2][c+2] != 15 or
                grid[r][c+2]+grid[r+1][c+1] + grid[r+2][c] !=15 ):
                return 0

            return 1


        res = 0
        for i in range(len(grid)-2):
            for j in range(len(grid[0])-2):
                res = res + magic(i,j)

        return res
        