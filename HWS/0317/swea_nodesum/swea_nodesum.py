import sys
sys.stdin= open('sample_input(3) (1).txt')

T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    node = [0]*(N+2)
    for _ in range(M):
        leaf = list(map(int, input().split()))
        node[leaf[0]] = leaf[1]
    print(node)

    for i in range(N, 0, -1):
        if node[i] == 0:
            node[i] = node[2*i] + node[2*i + 1]
    print(node)
    print(f'#{tc} {node[L]}')