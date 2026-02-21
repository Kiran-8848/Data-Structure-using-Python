def is_safe(maze, x, y, n, visited):
    # Check if (x, y) is inside maze and is path (1) and not visited
    return 0 <= x < n and 0 <= y < n and maze[x][y] == 1 and not visited[x][y]


def solve_maze(maze):
    n = len(maze)
    visited = [[False for _ in range(n)] for _ in range(n)]
    path = []

    def backtrack(x, y):
        # Base case: If destination is reached
        if x == n - 1 and y == n - 1:
            path.append((x, y))
            return True

        if is_safe(maze, x, y, n, visited):
            visited[x][y] = True
            path.append((x, y))

            # Move Down
            if backtrack(x + 1, y):
                return True

            # Move Right
            if backtrack(x, y + 1):
                return True

            # Move Up
            if backtrack(x - 1, y):
                return True

            # Move Left
            if backtrack(x, y - 1):
                return True

            # Backtracking step
            visited[x][y] = False
            path.pop()

        return False

    if backtrack(0, 0):
        return path
    else:
        return "No Path Found"


# Example Maze
maze = [
    [1, 0, 0, 0],
    [1, 1, 0, 1],
    [0, 1, 0, 0],
    [1, 1, 1, 1]
]

result = solve_maze(maze)
print(result)
#### slotion 2
def rIAm