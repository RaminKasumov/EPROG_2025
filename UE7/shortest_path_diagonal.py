from collections import deque

MOVES = [
    (1, 0), (-1, 0), (0, 1), (0, -1),
    (1, 1), (1, -1), (-1, 1), (-1, -1)
]

def in_bounds(x, y, n):
    return 0 <= x < n and 0 <= y < n

def bfs_with_diagonals(maze, start, goal):
    n = len(maze)
    dist = [[float('inf')] * n for _ in range(n)]
    parent = {}

    q = deque([start])
    dist[start[0]][start[1]] = 0

    while q:
        x, y = q.popleft()

        if (x, y) == goal:
            break

        for dx, dy in MOVES:
            nx, ny = x + dx, y + dy

            if in_bounds(nx, ny, n) and maze[nx][ny] == 0:
                if dist[nx][ny] == float('inf'):
                    dist[nx][ny] = dist[x][y] + 1
                    parent[(nx, ny)] = (x, y)
                    q.append((nx, ny))

    if dist[goal[0]][goal[1]] == float('inf'):
        return None

    path = []
    cur = goal

    while cur != start:
        path.append(cur)
        cur = parent[cur]

    path.append(start)
    path.reverse()
    return path