import random, sys, time, copy

# Constants
WIDTH, HEIGHT = 79, 20
ALIVE, DEAD = 'O', ' '

# Initialize grid
nextCells = {(x, y): ALIVE if random.random() < 0.5 else DEAD 
            for x in range(WIDTH) for y in range(HEIGHT)}

# Neighbor offsets
neighbors = [(-1,-1), (0,-1), (1,-1), 
             (-1, 0),         (1, 0),
             (-1, 1), (0, 1), (1, 1)]

while True:
    # Clear screen and copy cells
    print('\n' * 50)
    cells = copy.deepcopy(nextCells)
    
    # Print current state
    for y in range(HEIGHT):
        print(''.join(cells[(x, y)] for x in range(WIDTH)))
    print('Press Ctrl-C to quit.')
    
    # Calculate next generation
    for (x, y) in cells:
        # Count living neighbors
        alive_neighbors = sum(
            cells[((x+dx)%WIDTH, (y+dy)%HEIGHT)] == ALIVE 
            for (dx, dy) in neighbors
        )
        
        # Apply Conway's rules
        if (cells[(x, y)] == ALIVE and alive_neighbors in {2, 3}) or \
           (cells[(x, y)] == DEAD and alive_neighbors == 3):
            nextCells[(x, y)] = ALIVE
        else:
            nextCells[(x, y)] = DEAD
    
    time.sleep(0.1)  # Small delay to observe changes