# Advent of Code day 4
# -------------------Part 1-------------------
"""
This is similar to prefix sum so i will solve in 2 ways
"""

def get_directions():
    # 8 neighbors
    return [(-1,-1), (-1,0), (-1,1),
            (0,-1),         (0,1),
            (1,-1), (1,0), (1,1)]

def count_neighbors(grid, i, j):
    rows, cols = len(grid), len(grid[0])
    directions = get_directions()
    count = 0
    for dx, dy in directions:
        ni, nj = i + dx, j + dy
        if 0 <= ni < rows and 0 <= nj < cols:
            if grid[ni][nj] == '@':
                count += 1
    return count

def count_accessible_naive(grid):
    rows, cols = len(grid), len(grid[0])
    accessible_count = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '@' and count_neighbors(grid, i, j) < 4:
                accessible_count += 1
    return accessible_count

def read_grid(filename):
    with open(filename, "r") as f:
        # Convert each line to a list of characters
        return [list(line.strip()) for line in f if line.strip()]


grid = read_grid("inputs/input_day_4.txt")

print("-------------------Part 1-------------------")
print("Naive count:", count_accessible_naive(grid))

def increment_neighbors(neighbor_count, i, j):
    rows, cols = len(neighbor_count), len(neighbor_count[0])
    directions = get_directions()
    for dx, dy in directions:
        ni, nj = i + dx, j + dy
        if 0 <= ni < rows and 0 <= nj < cols:
            neighbor_count[ni][nj] += 1

def count_accessible_optimized(grid):
    rows, cols = len(grid), len(grid[0])
    neighbor_count = [[0]*cols for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '@':
                increment_neighbors(neighbor_count, i, j)

    accessible_count = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '@' and neighbor_count[i][j] < 4:
                accessible_count += 1

    return accessible_count

print("-------------------Part 1 optimized-------------------")
print("Optimized count:", count_accessible_optimized(grid))

# -------------------Part 2-------------------
"""
Again 2 approaches
reusing helper functions
+1 helper function 
"""
def remove_accessible_naive(grid):
    rows, cols = len(grid), len(grid[0])
    total_removed = 0
    changed = True
    
    while changed:
        changed = False
        to_remove = []

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '@' and count_neighbors(grid, i, j) < 4:
                    to_remove.append((i, j))
                    changed = True

        for i, j in to_remove:
            grid[i][j] = '.'
            total_removed += 1

    return total_removed

print("-------------------Part 2-------------------")
print("Naive count:", remove_accessible_naive(grid))

def decrement_neighbors(neighbor_count, i, j):
    rows, cols = len(neighbor_count), len(neighbor_count[0])
    directions = get_directions()
    for dx, dy in directions:
        ni, nj = i + dx, j + dy
        if 0 <= ni < rows and 0 <= nj < cols:
            neighbor_count[ni][nj] -= 1

def remove_accessible_optimized(grid):
    rows, cols = len(grid), len(grid[0])
    neighbor_count = [[0]*cols for _ in range(rows)]

    # Precompute neighbor counts
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '@':
                increment_neighbors(neighbor_count, i, j)

    total_removed = 0
    changed = True

    while changed:
        changed = False
        to_remove = []

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '@' and neighbor_count[i][j] < 4:
                    to_remove.append((i, j))
                    changed = True

        for i, j in to_remove:
            grid[i][j] = '.'
            total_removed += 1
            decrement_neighbors(neighbor_count, i, j)

    return total_removed

print("-------------------Part 2 optimized-------------------")
grid = read_grid("inputs/input_day_4.txt") # I updated the grid while removing so have to read again
print("Optimized count:", remove_accessible_optimized(grid))