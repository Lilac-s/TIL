from collections import deque

N, K = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())

queue = []

for i in range(N):
    for j in range(N):
        if grid[i][j] != 0:
            queue.append((grid[i][j], i, j, 0))

queue.sort()
queue = deque(queue)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while queue:
    virus, x, y, time = queue.popleft()
    if time == S:
        break
    for dp in range(4):
        nx = x + dx[dp]
        ny = y + dy[dp]
        if 0<=nx<N and 0<ny<N and grid[nx][ny] == 0:
            grid[nx][ny] = virus
            queue.append((virus, nx, ny, time+1))

print(grid[X-1][Y-1])