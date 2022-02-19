import sys
sys.stdin= open('input.txt')

T = int(input())
for tc in range(T):
    N = int(input())
    price_lst = list(map(int, input().split()))
    sol = 0
    max_index = price_lst[N-1]

    for i in range(N-2, -1, -1):
        if max_index < price_lst[i]:
            max_index = price_lst[i]
        else:
            sol += (max_index - price_lst[i])

    print(f'#{tc + 1} {sol}')




'''    sol = s = max_index =  0 # 처음 시작하는 리스트 인덱싱

    while s < N:
        max_index = s
        for i in range(s, N):
            if price_lst[max_index] < price_lst[i]:
                max_index = i
        for i in range(s, max_index):
            sol += price_lst[max_index] - price_lst[i]
        s = max_index + 1

    print(f'#{tc+1} {sol}')'''