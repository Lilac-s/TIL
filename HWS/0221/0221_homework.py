# import sys
# sys.stdin= open('sample_input.txt')

T = int(input())

for T in range(1, T+1):
    N = int(input())
    arr = [[1]*x for x in range(1, N+1)]

    for i in range(N):
        for j in range(N+1):
            if i >= 2 and j >= 1 and j < i:
                arr[i][j] = arr[i-1][j-1] + arr[i-1][j]

    print(f'#{T}')
    for a in arr:
        print(*a)