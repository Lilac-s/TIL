import sys
sys.stdin= open('sample_input(2).txt')

T = int(input())
for tc in range(1, T+1): # testcase 입력받고 for문으로 반복
    V, E = map(int, input().split())
    load_grid = [[0] * (V+1) for grid in range(V+1)] # 지나가는 경로는 1로 표시해 줄 그리드 만들기
    # Ai = [list(map(int, input().split())) for _ in range(E)]
    for i in range(E):
        a, b = map(int, input().split())
        load_grid[a][b] = 1 # 지나가는 경로를 1로 표시해 준다.
    S, G = map(int, input().split())
    # print(V)
    # print(E)
    # print(Ai)
    # print(S)
    # print(G)
    # print(load_grid)

    # for A in Ai:
    #     load_grid[A[0]-1][A[1]-1] = 1
    #     load_grid[A[1]-1][A[0]-1] = 1
    # print(load_grid)
    stack = [S]
    visited = [S] # 출발하는 노드를 넣어 둔다.

    while stack:
        tmp = stack[-1]
        for node in range(1, V+1):
            if load_grid[tmp][node] == 1 and node not in visited:
                visited.append(node)
                stack.append(node)
                break
        else:
            stack.pop() # 출발 노드에서 도착 노드까지 확인한다.

    if G in visited:
        ans = 1
    else:
        ans = 0

    print(f'#{tc} {ans}') # 출력문

