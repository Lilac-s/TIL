T = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for tc in range(1, T+1):
    H, W = map(int, input().split())
    grid = [list(input()) for _ in range(H)]

    x = 0
    y = 0
    while x < W and y < H:
        if grid[x][y] == '#':
            grid[x][y] = '.'
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0<=nx<W and 0<=ny<H and grid[nx][ny] == '#':
                    x = nx
                    y = ny
        else:
            x += 1
            y += 1
    print(grid)