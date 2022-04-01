def dfs(x):
    global res
    if x == N: # X가 N과 같을 만큼 퀸을 다 놓았다면
        res += 1 # 하나의 경우의 수를 추가해 준다.
        return
    for i in range(N):
        grid[x] = i # 하나씩 퀸을 놓아 봄
        if queen(x): # 문제 없으면
            dfs(x+1) # 하나씩 늘려가면서 재귀 (놓을 수 있는 만큼 가지가 늘어난다)

def queen(x): # 퀸이 잡을 수 있는지 확인하는 함수
    for i in range(x):
        if grid[x] == grid[i] or abs(grid[i]-grid[x]) == x-i:
            return False
    return True

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    grid = [[0]*N for _ in range(N)]
    res = 0
    dfs(0)
    print(f'#{tc} {res}')