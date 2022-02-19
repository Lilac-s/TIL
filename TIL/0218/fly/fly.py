import sys
sys.stdin= open('input.txt')

T = int(input())
for tc in range(1, T+1):

    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    sol = 0

    for r in range(N-M+1):
        for c in range(N-M+1):
            cnt = 0
            for rr in range(r, r+M):
                for cc in range(c, c+M):
                    cnt += arr[cc][rr]
            if sol < cnt:
                sol = cnt
    print(f'#{tc} {sol}')

