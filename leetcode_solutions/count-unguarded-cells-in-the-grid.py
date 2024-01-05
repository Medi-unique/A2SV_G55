# class Solution:
    
#     def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
#         counts = {(r, c): 0 for r in range(m) for c in range(n)}
#         directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
#         for guard in guards:
#             r, c = guard
#             for dr, dc in directions:
#                 nr, nc = r + dr, c + dc
#                 while 0 <= nr < m and 0 <= nc < n and [nr, nc] not in walls:
#                     counts[(nr, nc)] += 1
#                     nr, nc = nr + dr, nc + dc
                    
#         for wall in walls:
#             counts[(wall[0], wall[1])] = float('inf')
            
#         return sum(1 for count in counts.values() if count == 0)

class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        space = [['e' for _ in range(n)] for _ in range(m)]
        empty = m*n - len(guards) - len(walls)
        for guard in guards:
            space[guard[0]][guard[1]] = 'o'

        for wall in walls:
            space[wall[0]][wall[1]] = 'o'

        def walk(r, c):
            for dx, dy in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
                row, col = r + dy, c + dx

                while row >= 0 and row < m and col >= 0 and col < n:
                    if space[row][col] == 'e':
                        space[row][col] = 'g'
                        nonlocal empty
                        empty -= 1
                    elif space[row][col] == 'o':
                        break
                    row, col = row + dy, col + dx

        for guard in guards:
            walk(guard[0], guard[1])

        return empty