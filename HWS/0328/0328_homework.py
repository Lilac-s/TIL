# swea_최소합

import sys
sys.stdin= open('sample_input (4).txt')

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, cnt):
    global res
    if res < cnt:
        return
    if x == N-1 and y == N-1:
        res = cnt
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
            visited[nx][ny] = 1
            cnt += grid[nx][ny]
            dfs(nx, ny, cnt)
            visited[nx][ny] = 0
            cnt -= grid[nx][ny]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    res = 1e9
    x = 0
    y = 0
    dfs(x, y, grid[x][y])
    print(f'#{tc} {res}')
