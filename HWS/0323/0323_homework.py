# boj_17836
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs():
    gram = int(1e9)
    q.append((0, 0))
    visited[0][0] = 1
    while q:
        x, y = q.popleft()
        if (x, y) == (N-1, M-1):
            return min(visited[x][y]-1, gram)
        if miro[x][y] == 2: # 그람이 찾아졌을때
            gram = visited[x][y]-1 + N-1-x + M-1-y # 직선거리 더해서 반환
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                if miro[nx][ny] == 0 or miro[nx][ny] == 2:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))
    return gram

N, M, T = map(int, input().split())
miro = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
q = deque()

res = bfs()
if res > T:
    print('Fail')
else:
    print(res)