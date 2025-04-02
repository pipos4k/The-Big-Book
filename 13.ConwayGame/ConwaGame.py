# Conway's Game
import random

WIDTH = 70
HEIGHT = 20

cells = {}
for i in range(WIDTH):
    for j in range(HEIGHT):
        cells[(i, j)] = " " if random.randint(0, 1) else "0"

for j in range(20):
    print("".join(cells[(i, j)] for i in range(70)))

neighbor_offsets = [(-1,-1), (0,-1), (1,-1), (-1,0), (1,0), (-1,1), (0,1), (1,1)]

for x in range(WIDTH):
    for y in range(HEIGHT):
        alive = cells[(x, y)] == "0"
        count = sum(cells[((x+dx)%WIDTH, (y+dy)%HEIGHT)] == "0" for dx, dy in neighbor_offsets)
        cells[(x, y)] = "0" if (alive and count in {2,3}) or (not alive and count == 3) else " "
