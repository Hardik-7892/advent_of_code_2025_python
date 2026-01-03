# Advent of Code day 4
# -------------------Part 1-------------------
"""
This is similar to prefix sum so i will solve in 2 ways
"""
def count_neighbors(grid, i, j):
    rows, cols = len(grid), len(grid[0])
    directions = [(-1,-1), (-1,0), (-1,1),
                  (0,-1),         (0,1),
                  (1,-1), (1,0), (1,1)]
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
        return [line.strip() for line in f if line.strip()]

grid = read_grid("inputs/input_day_4.txt")

print("-------------------Part 1-------------------")
print("Naive count:", count_accessible_naive(grid))

def increment_neighbors(grid, neighbor_count, i, j):
    rows, cols = len(grid), len(grid[0])
    directions = [(-1,-1), (-1,0), (-1,1),
                  (0,-1),         (0,1),
                  (1,-1), (1,0), (1,1)]
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
                increment_neighbors(grid, neighbor_count, i, j)

    accessible_count = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '@' and neighbor_count[i][j] < 4:
                accessible_count += 1

    return accessible_count

print("-------------------Part 1 optimized-------------------")
print("Optimized count:", count_accessible_optimized(grid))